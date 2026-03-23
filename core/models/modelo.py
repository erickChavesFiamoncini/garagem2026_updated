from django.db import models


class Modelo(models.Model):
    nome = models.CharField(max_length=80)
    marca = models.CharField(max_length=80, null=True, blank=True)
    categoria = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        marca = self.marca.upper() if self.marca else ''
        nome = self.nome.upper() if self.nome else ''
        return f'({self.id}) {marca} {nome}'
