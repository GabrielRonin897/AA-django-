from django.shortcuts import render
from .models import Produto


# Create your views here.
"""
def home(request):
    
    tipos_valor=[1.50,1.00,2.00]
    tipos_nome=["pão de doce", "pão de sal","pão de quijo"]
    
    return render(request, "padaria/home.html",{"tipos_nome":tipos_nome,"tipo_valor": tipos_valor})
"""
def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'padaria/produtos.html', {'produtos': produtos})

def processar_pedido(request):
    if request.method == 'POST':
        produto_id = request.POST['produto']
        quantidade = request.POST['quantidade']
        produto = Produto.objects.get(pk=produto_id)
        valor_total = produto.preco * int(quantidade)
        return render(request, 'confirmar_pedido.html', {'produto': produto, 'quantidade': quantidade, 'valor_total': valor_total})
    else:
        return render(request, 'erro.html', {'mensagem': 'Método não permitido'})
