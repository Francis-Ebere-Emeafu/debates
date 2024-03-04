from django.urls import path
from .views import (
    ProfileList, ProfileDetails,
    UserList, UserDetail
    )


urlpatterns = [
    path('users/', UserList.as_view(), name='users'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('', ProfileList.as_view(), name='profile'),
    path('<int:pk>/', ProfileDetails.as_view(),name='profile-details'),
    
]
