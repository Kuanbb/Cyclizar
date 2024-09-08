from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=25, null=False, unique=True)
    email = models.EmailField(null=False)
    def __unicode__(self):
        return self.nome
