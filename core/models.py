from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario

# Create your models here.

class PontoTuristico(models.Model):
	nome = models.CharField(max_length=150)
	descricao = models.TextField(max_length=300)
	aprovado = models.BooleanField(default=False)
	atracoes = models.ManyToManyField(Atracao)
	comentarios = models.ManyToManyField(Comentario)

	def __str__(self):
		return self.nome