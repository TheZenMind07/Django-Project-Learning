from django.db import models

# Create your models here.
class Product(models.Model):
  name =            models.CharField(max_length=40)
  description =     models.TextField(blank=True, null=True)
  rating =          models.DecimalField(decimal_places=0, max_digits=2)
  price =           models.DecimalField(decimal_places=2, max_digits=10)
  feature =         models.BooleanField()