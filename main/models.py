from django.db import models

class Item(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField(default=1)
    comprado = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
