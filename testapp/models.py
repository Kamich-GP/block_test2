from django.db import models


# Create your models here.
class Question(models.Model):
    name = models.TextField()


    def __str__(self):
        return str(self.name)
