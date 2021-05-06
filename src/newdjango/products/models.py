from django.db import models

# Create your models here.
class Product(models.Model):
  name =            models.TextField()
  description =     models.TextField()
  rating =          models.TextField()
  price =           models.TextField()