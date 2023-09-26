from django.db import models

# Create your models here.
class Worker(models.Model):
    worker_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    whatsapp = models.BooleanField(default=False)
    available = models.BooleanField(default=True)