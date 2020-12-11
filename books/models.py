from django.db import models


class Books(models.Model):
    numero_processo = models.CharField(max_length=50)
    unidade = models.CharField(max_length=50)
    orgao_julgador = models.CharField(max_length=255)
    classe = models.CharField(max_length=50)
    assunto_principal =  models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    data_criacao = models.DateField(auto_now_add=True)
    