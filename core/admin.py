from django.contrib import admin

from . import models


# Register your models here.
admin.site.register(models.Taxonomy)
admin.site.register(models.Taxon)
