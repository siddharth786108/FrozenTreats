from django.db import models
class submit(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=40)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
