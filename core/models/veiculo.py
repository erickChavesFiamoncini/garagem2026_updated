from django.db import models

from .acessorio import Acessorio
from .cor import Cor
from .modelo import Modelo


class Veiculo(models.Model):
    ano = models.IntegerField(default=0, blank=True, null=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True)
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name='veiculos', null=True, blank=True)
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name='veiculos', null=True, blank=True)
    acessorios = models.ManyToManyField(Acessorio, related_name='veiculos')

    def __str__(self):
        return f'({self.id}) - {self.modelo} - {self.cor} - {self.ano}'
