from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify



# Create your models here.




class Questions(models.Model):      
    question = models.CharField(_('question'),max_length = 200)
    first_option = models.CharField(_('first_option'),max_length=200)
    second_option = models.CharField(_('second_option'),max_length=200)
    slug = models.SlugField(null=True,blank=True)
    
    
    
    
    
    
   



    
    
    def __str__(self):
        return self.question
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.question)
        
        super(Questions, self).save(*args, **kwargs)
        
        
        
