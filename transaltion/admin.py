from django.contrib import admin
from django.contrib import admin
from tof.admin import TofAdmin, TranslationTabularInline
from tof.decorators import tof_prefetch
from .models import Questions

# Register your models here.



class QuestionsAdmin(TofAdmin):
    list_display = ('question', 'first_option', 'second_option','third_option','fourth_option','short_answer','correct_answer','order')
    search_fields = ('question', )
    inlines = (TranslationTabularInline, )
    
    
    
    @tof_prefetch('question')
    def get_queryset(self, request):
        return super().get_queryset(request)




from .models import Vintage, Wine, Winery


@admin.register(Winery)
class WineryAdmin(TofAdmin):
    """Example translatable field №3
    This class is example where you can see Tabular inline
    Attributes:
        list_display: [description]
        search_fields: [description]
        inlines
    """
    list_display = ('title', 'description', 'sort')
    search_fields = ('title', )
    inlines = (TranslationTabularInline, )


@admin.register(Wine)
class WineAdmin(TofAdmin):
    """Example translatable field №2
    This class is example where translatable field save values to all added languages
    Attributes:
        list_display: [description]
        search_fields: [description]
        form: [description]
    """
    list_display = ('title', 'description', 'active', 'sort')
    search_fields = ('title', )
    only_current_lang = ('description', )


@admin.register(Vintage)
class VintageAdmin(admin.ModelAdmin):
    """Example translatable field №1
    This class is example where translatable field save value only in current language
    Attributes:
        list_display: [description]
    """
    list_display = search_fields = ('wine__title', 'year', 'description')

    def wine__title(self, obj, *args, **kwargs):
        return obj.wine.title

    @tof_prefetch('wine')
    def get_queryset(self, request):
        return super().get_queryset(request)


    
    
    

admin.site.register(Questions,QuestionsAdmin)