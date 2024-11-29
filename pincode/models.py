from django.db import models

class Pin(models.Model):
    code = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.code[:10]