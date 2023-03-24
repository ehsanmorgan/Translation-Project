from django.contrib import admin
from tof.admin import TofAdmin, TranslationTabularInline
from tof.decorators import tof_prefetch
from .models import Questions

# Register your models here.



class QuestionsAdmin(TofAdmin):
    list_display = ('question', 'first_option', 'second_option','third_option','fourth_option','short_answer','correct_answer','order')
    search_fields = ('question', )
    inlines = (TranslationTabularInline, )
    
    
    
    


admin.site.register(Questions,QuestionsAdmin)