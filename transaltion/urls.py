from django.urls import path
from .views import home


app_name='transaltion'

urlpatterns = [
    path('',home,name='home')
    
]
