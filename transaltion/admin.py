from django.contrib import admin
#from tof.admin import TofAdmin, TranslationTabularInline
#from tof.decorators import tof_prefetch
from .models import Questions
from modeltranslation.admin import TranslationAdmin





class adminquestion(TranslationAdmin):
    pass


admin.site.register(Questions)

    
    
    
    
