from django.db import models

# Create your models here.
import email
from django.db import models

# Create your models here.
class customer(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.name  