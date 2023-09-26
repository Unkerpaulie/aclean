from django.db import models

# Create your models here.
class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    whatsapp = models.BooleanField(default=False)


