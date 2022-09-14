from django.db import models

class Beverages(models.Model):
    name=models.CharField(max_length=200)
    desc=models.CharField(max_length=600)

    def __str__(self) -> str:
        return self.name
