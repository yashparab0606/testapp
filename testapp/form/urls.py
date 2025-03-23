from django.urls import path
from .views import register, user_login, user_logout, user_home

urlpatterns = [
    path('', user_home, name="home"),  # Empty path for the home page
    path('register/', register, name="register"),
    path('login/', user_login, name="login"),
    path('logout/', user_logout, name="logout"),
]
