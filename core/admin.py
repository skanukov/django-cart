import json
import logging

from django import http
from django.conf import urls
from django.contrib import admin
from django.db import connection
from django.utils import html

from . import models


# Get an instance of a logger.
logger = logging.getLogger(__name__)


# Register your models here.
@admin.register(models.Taxonomy)
class TaxonomyAdmin(admin.ModelAdmin):
    list_display = ('drag_handle', 'position', 'name', 'visible',)
    list_display_links = ('name',)
    ordering = ('-position',)

    def drag_handle(self, obj):
        return html.format_html('&#9776;')
    drag_handle.short_description = ''

    def get_urls(self):
        existing_urls = super(TaxonomyAdmin, self).get_urls()
        my_urls = [
            urls.url(r'^reorder/$',
                self.admin_site.admin_view(self.reorder))
        ]
        return my_urls + existing_urls

    def reorder(self, request):
        req_data = json.loads(request.body.decode('utf-8'))
        logger.warning('Request data json is: {}'.format(req_data))
        
        ids = []
        positions = []
        for obj_data_str in req_data:
            obj_data = json.loads(obj_data_str)
            ids.append(obj_data['id'])
            positions.append(obj_data['position'])
        
        # Reverse sort the positions array.
        positions = sorted(positions, reverse=True)
        logger.warning('Sorted positions are: {}'.format(positions))
        
        # Make a dict from ids and reverse sorted positions.
        reorder_data = dict(zip(ids, positions))
        logger.warning('Reorder data is: {}'.format(reorder_data))
        
        # Build the sql clause to update database records.
        sql_update_builder = [
            'UPDATE core_taxonomy',
            'SET position = (',
                'SELECT tmp.position',
                'FROM (',
        ]
        sql_params = []
        
        for k, v in reorder_data.items():
            sql_update_builder.extend([
                'SELECT %s AS id, %s AS position',
                'UNION',
            ])
            sql_params.append(k)
            sql_params.append(v)

        # Remove last 'UNION' statement.
        sql_update_builder.pop()
            
        sql_update_builder.extend([
                ') AS tmp',
                'WHERE tmp.id = core_taxonomy.id',
            ')',
        ])
        sql_update = ' '.join(sql_update_builder)
        logger.warning(sql_update)
        logger.warning(sql_params)
        
        # Execute the sql.
        with connection.cursor() as cursor:
            cursor.execute(sql_update, sql_params)

        return http.JsonResponse({'status': 'ok'})

    class Media:
        css = {
            'all': ('css/admin/sort.css',)
        }
        js = ('js/admin/csrfajax.js', 'js/admin/Sortable.min.js',
              'js/admin/sort.js',)


@admin.register(models.Taxon)
class TaxonAdmin(admin.ModelAdmin):
    pass
