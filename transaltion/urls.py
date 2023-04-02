from django.urls import path
from .views import home ,test_translation


app_name='transaltion'

urlpatterns = [
    path('',home,name='home'),
    path('test',test_translation,name='test_translation'),
    
]
