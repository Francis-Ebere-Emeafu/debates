from django.contrib.auth import get_user_model
from rest_framework import generics
from .serializers import ProfileSerializer, UserSerializer, CategorySerializer
from .models import Profile, Category


class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetails(generics.RetrieveUpdateAPIView, generics.RetrieveDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateAPIView, generics.RetrieveDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class CategoryView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryDetails(generics.RetrieveUpdateAPIView, generics.RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
