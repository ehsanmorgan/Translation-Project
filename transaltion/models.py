from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

# Create your models here.



class Questions(models.Model):
    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('question-plural')
        ordering = ('sort', )
        
    question = models.CharField(_('question'),max_length = 200)
    first_option = models.CharField(_('first_option'),max_length=200)
    second_option = models.CharField(_('second_option'),max_length=200)
    third_option = models.CharField(_('third_option'),max_length=200)
    fourth_option = models.CharField(_('fourth_option'),max_length=200)
    short_answer = models.TextField(_('short_answer'),max_length=1000)
    correct_answer = models.CharField(_('correct_answer'),max_length=200)
    order = models.IntegerField(_('order'),)
    slug = models.SlugField(null=True,blank=True)
    sort = models.IntegerField(_('Sort'), default=0, blank=True, null=True)
    active = models.BooleanField(_('Active'), default=False)
    
    
    
    
    
    
    
    def __str__(self):
        return self.question
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.question)
        super(Questions, self).save(*args, **kwargs)
        
        
        
class Winery(models.Model):
    class Meta:
        verbose_name = _('Winery')
        verbose_name_plural = _('Winery-plural')
        ordering = ('sort', )

    title = models.CharField(_('Title'), max_length=250, default='', blank=True, null=False)
    description = models.TextField(_('Description'), null=True, blank=True)
    sort = models.IntegerField(_('Sort'), default=0, blank=True, null=True)


class Wine(models.Model):
    class Meta:
        verbose_name = _('wine')
        verbose_name_plural = _('wine-plural')
        ordering = ('sort', )

    title = models.CharField(_('Title'), max_length=250, default='', blank=True, null=False)
    description = models.TextField(_('Description'), null=True, blank=True)
    active = models.BooleanField(_('Active'), default=False)
    sort = models.IntegerField(_('Sort'), default=0, blank=True, null=True)

    temperature_from = models.FloatField(_('Temperature_from'), help_text=_('in ° C'), null=True, blank=True)
    temperature_to = models.FloatField(_('Temperature_to'), help_text=_('in ° C'), null=True, blank=True)


class Vintage(models.Model):
    wine = models.ForeignKey(Wine, related_name='vintages', on_delete=models.CASCADE)
    year = models.IntegerField(_('Year'), default=0)
    description = models.TextField(_('Description'), null=True, blank=True)
