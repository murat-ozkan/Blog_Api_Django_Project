from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = [
            # "password",
            "date_joined",
            "groups",
            "last_login",
            "user_permissions"
            ]