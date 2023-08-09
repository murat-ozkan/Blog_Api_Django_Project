from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.category + "/" + self.title