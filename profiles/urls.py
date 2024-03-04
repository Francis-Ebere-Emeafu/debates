from django.urls import path
from .views import (
    ProfileList, ProfileDetails,
    UserList, UserDetail, CategoryView,
    CategoryDetails
    )


urlpatterns = [
    path('users/', UserList.as_view(), name='users'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('profiles', ProfileList.as_view(), name='profile'),
    path('profiles/<int:pk>/', ProfileDetails.as_view(),name='profile-details'),
    path('categories/', CategoryView.as_view(), name="category"),
    path('categories/<int:pk>/', CategoryDetails.as_view(), name='category-details')
]
