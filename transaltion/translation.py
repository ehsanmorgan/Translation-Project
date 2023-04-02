from modeltranslation.translator import translator, TranslationOptions
from .models import Questions




class questionsTranslation(TranslationOptions):
   
    fields=('question','first_option','second_option','third_option','fourth_option','short_answer','correct_answer')
    
    
    
translator.register(Questions, questionsTranslation)