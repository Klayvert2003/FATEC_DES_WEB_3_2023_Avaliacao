from django.db import models

class RegistroPresenca(models.Model):
    nome_aluno = models.CharField(max_length=100)
    nome_professor = models.CharField(max_length=100)
    curso_aluno = models.CharField(max_length=3)
    data_registro = models.DateTimeField(auto_now_add=True)
