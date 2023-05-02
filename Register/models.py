from django.db import models

# Create your models here.

class Myreg(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    whatsapp = models.IntegerField()
    location = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.fname