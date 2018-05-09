from django.db import models

# Create your models here.

class TODO(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    deadline = models.DateField()
    progress = models.IntegerField()


    def __str__(self):
        return self.title + '-' + self.description


