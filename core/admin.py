from django.conf import urls
from django.contrib import admin
from django import http
from django.utils import html

from . import models


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
        return http.JsonResponse({'status': 'ok'})

    class Media:
        css = {
            'all': ('css/admin/sort.css',)
        }
        js = ('js/admin/Sortable.min.js', 'js/admin/sort.js',)


@admin.register(models.Taxon)
class TaxonAdmin(admin.ModelAdmin):
    pass
