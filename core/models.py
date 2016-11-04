from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Taxonomy(models.Model):
    name = models.CharField(max_length=200)
    position = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Taxonomy')
        verbose_name_plural = _('Taxonomies')


class Taxon(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True)
    permalink = models.URLField(max_length=200, null=True, blank=True)
    position = models.IntegerField(default=0)
    meta_title = models.CharField(max_length=500, null=True, blank=True)
    meta_keywords = models.CharField(max_length=500, null=True, blank=True)
    meta_description = models.CharField(max_length=500, null=True, blank=True)

    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True,
                                       blank=True)
    taxonomy = models.ForeignKey(Taxonomy, on_delete=models.CASCADE) 

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Taxon')
        verbose_name_plural = _('Taxons')
