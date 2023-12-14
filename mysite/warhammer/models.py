from django.db import models

# Create your models here.

class NewBuy(models.Model):
    def __str__(self):
        return self.product
    product = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    price = models.FloatField()
    tags = models.TextField(max_length=2000)
    image = models.CharField(max_length=500)

class usedBuy(models.Model):
    def __str__(self):
        return self.product
    product = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    price = models.FloatField()
    condition = models.CharField(max_length=200)
    seller = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.IntegerField()


class checkout(models.Model):
    def __str__(self):
        return self.product
    product = models.CharField(max_length=200)
    price = models.FloatField()
    type = models.CharField(max_length=200)

