from django.db import models

class Login(models.Model):
    number = models.CharField(max_length=100, null=True)
    jeton_N = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.jeton_N[:10]