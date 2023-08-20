from django.urls import path
from users.views import hello_users, getAllUsers, create_user

urlpatterns = [
    path('hello', hello_users),
    path('getall', getAllUsers),
    path('create', create_user),
]