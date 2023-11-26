
from django.contrib import admin
from django.urls import include, path
from django.views import criar_pedido

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app_padaria/', include('app_padaria.urls')),
    path('criar_pedido/', criar_pedido, name='criar_pedido'),
]

