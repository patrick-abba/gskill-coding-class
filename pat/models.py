from django.db import models
import uuid

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

    
    

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    price = models.FloatField(null=False)
    category = models.TextField(null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=200, null=False, blank=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
   
    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=100, null=True)
    price = models.FloatField(null=False)
    category = models.TextField(null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=200, null=False, blank=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name
