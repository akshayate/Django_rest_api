from django.db import models

# Create your models here.

class apiModels(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)

    def __str__(self):
        return self.title
