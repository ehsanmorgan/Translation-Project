from modeltranslation.translator import translator, TranslationOptions
from .models import Questions




class questionsTranslation(TranslationOptions):
   
    fields=('question','first_option','second_option')
    
    
    
translator.register(Questions,questionsTranslation)