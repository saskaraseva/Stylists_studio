from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    class Meta():
        db_table = 'client'
    client_id = models.BigAutoField
    client_name = models.CharField(max_length=100)
    client_phone = models.CharField(max_length=100)

