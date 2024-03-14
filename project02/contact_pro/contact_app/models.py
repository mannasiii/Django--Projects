from django.db import models

# Create your models here.
class Msg(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150) # models.CharField(max_length=100)
    mobile= models.BigIntegerField()
    msg = models.TextField() # size field not required
    

