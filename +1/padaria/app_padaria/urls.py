
from django.contrib import admin
from django.urls import path
from .views import criar_pedido

urlpatterns = [
    path('admin/', admin.site.urls),
    path('criar_pedido/', criar_pedido, name='criar_pedido'),
]
