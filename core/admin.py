from django.contrib import admin

from . import models


# Register your models here.
@admin.register(models.Taxonomy)
class TaxonomyAdmin(admin.ModelAdmin):
    class Media:
        js = ("taxonomy-index.js",)


@admin.register(models.Taxon)
class TaxonomyAdmin(admin.ModelAdmin):
    pass
