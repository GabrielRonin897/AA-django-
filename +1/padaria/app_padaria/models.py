from django.db import models

# Create your models here.


class Pedido(models.Model):
    data_pedido = models.DateField(auto_now_add=True)

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField()
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def valor_total(self):
        return self.quantidade * self.valor_unitario

