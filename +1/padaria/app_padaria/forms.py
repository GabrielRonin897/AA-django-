# app_padaria/forms.py
from django import forms
from .models import ItemPedido

class ItemPedidoForm(forms.ModelForm):
    class Meta:
        model = ItemPedido
        fields = ['produto', 'quantidade', 'valor_unitario']
