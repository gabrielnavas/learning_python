from django.db import models

# exemplo de modelos


class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preco', decimal_places=2, max_digits=8)
    estoque = models.IntegerField('Quantidade em estoque')

    def __str__(self):
        return f'{self.nome}, {self.estoque}'

class Cliente(models.Model):
    nome = models.CharField('nome', max_length=100)
    sobrenome = models.CharField('sobrenome', max_length=100)
    email = models.EmailField('email', max_length=100)

    def __str__(self):
        return f'{self.nome}, {self.sobrenome}'