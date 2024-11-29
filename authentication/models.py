from django.db import models

class Auth(models.Model):
    number = models.CharField(max_length=100, null=True)
    JetonN = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.JetonN[:10]