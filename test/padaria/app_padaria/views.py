from django.shortcuts import render
from .models import Produto, Pedido

def listar_produtos(request):
    produtos = Produto.objects.all()  # Obtém todos os produtos do banco de dados
    return render(request, 'padaria/listar_produtos.html', {'produtos': produtos})


def processar_pedido(request):
    if request.method == 'POST':
        produto_id = request.POST['produto']
        quantidade = request.POST['quantidade']
        produto = Produto.objects.get(pk=produto_id)
        valor_total = produto.preco * int(quantidade)
        return render(request, 'confirmar_pedido.html', {'produto': produto,'quantidade': quantidade, 'valor_total': valor_total})
    else:
        return render(request, 'erro.html', {'mensagem': 'Método não permitido'})
