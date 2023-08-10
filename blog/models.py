from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(verbose_name="Category Names",max_length=64)
    
    class Meta:
        verbose_name = "Blog Category"
        verbose_name_plural = "Blog Categories"

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(verbose_name="Create Date(Optional)", max_length=128)
    content = models.TextField()
    created_date = models.DateTimeField(verbose_name="Create Date(Optional)", auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, verbose_name="Category", on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        # return self.category + "/" + self.title # Bu olmuyor. Bir obje ile string birleştirilemez. Aşağıdaki gibi fstr kullan.
        return f'{self.category} / {self.title}'