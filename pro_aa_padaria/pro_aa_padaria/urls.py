

from django.urls import path
from app_padaria import views

urlpatterns = [
    path('', views.home,name='home'),
    
]
