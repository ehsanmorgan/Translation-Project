from django.contrib import admin
#from tof.admin import TofAdmin, TranslationTabularInline
#from tof.decorators import tof_prefetch
from .models import Questions
from modeltranslation.admin import TranslationAdmin






@admin.register(Questions)

class NewsAdmin(TranslationAdmin):
    list_display=('question','first_option','second_option')
    group_fieldsets = True
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


    
    
    
    
