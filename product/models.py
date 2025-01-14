from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100 , unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2 , max_digits=10)
    category = models.ForeignKey("Category" , on_delete=models.CASCADE , null=True , blank=True)
    tags = models.ManyToManyField("Tag")

    def __str__(self):
        return f"{self.name}"
    
    
class Category(models.Model):
    name = models.CharField(max_length=100 , unique=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
