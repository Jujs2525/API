from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome
    
class Produto(models.Model):
    Nome Completo= models.CharField(max_length=100)
    Turma = models.TextField()
    Telefone = models.DecimalField(max_digits=10, decimal_places=2)
    Email = models.ForeignKey(Categoria, related_name='produtos',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome