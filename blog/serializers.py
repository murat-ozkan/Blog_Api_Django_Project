from rest_framework import serializers
from .models import Post, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = []

class PostSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField() # Bu 2 satır yazılmadan önce user ve category 1 olarak geliyordu. İsim gelmiyordu.
    category = serializers.StringRelatedField() # Bu 2 satır sayedinde ilişkisel tablodan veriyi aldı. Yani class Category self.name

    user_id = serializers.IntegerField() # Bu 2 satır da user_id ve category_id için gerekli.
    category_id = serializers.IntegerField()

    class Meta:
        model = Post
        exclude = []
        # exclude = [
        #     created_date,
        #     updated_date
        #     ]