from django.db import models

# Create your models here.
class Destinations(models.Model):
    
    name = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='Pictures', null=True , blank=True)
    desc = models.TextField(null=True)
    price = models.IntegerField(null=True)
    offer = models.BooleanField(default=False)



