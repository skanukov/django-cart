from django.db import models
from django.db.models import signals
from django import dispatch
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Taxonomy(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('name'))
    position = models.IntegerField(default=0, verbose_name=_('position'))
    visible = models.BooleanField(default=False, verbose_name=_('visible'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('taxonomy')
        verbose_name_plural = _('taxonomies')


class Taxon(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('name'))
    description = models.TextField(null=True, blank=True,
                                   verbose_name=_('description'))
    image = models.CharField(max_length=200, null=True, blank=True)
    permalink = models.URLField(max_length=200, null=True, blank=True,
                                verbose_name=_('permalink'))
    position = models.IntegerField(default=0, verbose_name=_('position'))
    visible = models.BooleanField(default=False, verbose_name=_('visible'))
    meta_title = models.CharField(max_length=500, null=True, blank=True)
    meta_keywords = models.CharField(max_length=500, null=True, blank=True)
    meta_description = models.CharField(max_length=500, null=True, blank=True)

    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True,
                               blank=True, verbose_name=_('parent'))
    taxonomy = models.ForeignKey(Taxonomy, on_delete=models.CASCADE,
                                 verbose_name=_('taxonomy'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('taxon')
        verbose_name_plural = _('taxons')


@dispatch.receiver(signals.post_save, sender=Taxonomy)
@dispatch.receiver(signals.post_save, sender=Taxon)
def taxonomy_post_create(sender, instance, created, **kwargs):
    # Set taxonomy position to it's id after creation.
    if created:
        id = instance.pk
        instance.position = id
        instance.save()
