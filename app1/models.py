from django.db import models

class employee(models.Model):
    name=models.CharField(max_length=20)
