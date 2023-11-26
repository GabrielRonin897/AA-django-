from django.contrib import admin
from django.urls import path
from views import lista_produtos
from models import Produto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('produtos/', lista_produtos, name='lista_produtos'),
]