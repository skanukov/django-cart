from django.contrib import admin
from django.utils import html

from . import models


# Register your models here.
@admin.register(models.Taxonomy)
class TaxonomyAdmin(admin.ModelAdmin):
    list_display = ('drag_handle', 'name', 'visible')
    list_display_links = ('name',)

    def drag_handle(self, obj):
        return html.format_html('&#9776;')
    drag_handle.short_description = ''

    class Media:
        css = {
            'all': ('css/admin/sort.css',)
        }
        js = ('js/admin/Sortable.min.js', 'js/admin/sort.js',)


@admin.register(models.Taxon)
class TaxonomyAdmin(admin.ModelAdmin):
    pass
