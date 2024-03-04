from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Profile, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            "name",
            "phone_number",
            "sex",
            "image",
            "birth_date",
            "category",  # Include the category field
        ]
        extra_kwargs = {
            'category': {'read_only': False}  # Allow users to select a category
        }
        depth = 1


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)
