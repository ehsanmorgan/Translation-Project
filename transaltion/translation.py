from modeltranslation.translator import TranslationOptions,register
from .models import Questions



@register(Questions)
class questionsTranslation(TranslationOptions):
    fields=('question','first_option','second_option','third_option')