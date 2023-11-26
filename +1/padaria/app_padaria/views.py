from django.shortcuts import render, redirect
from .forms import ItemPedidoForm
from .models import Pedido, ItemPedido

def criar_pedido(request):
    if request.method == 'POST':
        form = ItemPedidoForm(request.POST)
        if form.is_valid():
            item_pedido = form.save(commit=False)
            pedido, created = Pedido.objects.get_or_create(data_pedido=item_pedido.pedido.data_pedido)
            item_pedido.pedido = pedido
            item_pedido.save()
            return redirect('criar_pedido')
    else:
        form = ItemPedidoForm()
    
    pedidos = Pedido.objects.all()
    itens_pedido = ItemPedido.objects.all()
    return render(request, 'app_padaria/criar_pedido.html', {'form': form, 'pedidos': pedidos, 'itens_pedido': itens_pedido})
