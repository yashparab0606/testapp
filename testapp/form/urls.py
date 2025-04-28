from django.urls import path
from .views import register, user_login, user_logout, home_view

urlpatterns = [
    path('', home_view, name='home_view'),    # Empty path for the home page
    path('register/', register, name="register"),
    path('login/', user_login, name="login"),
    path('logout/', user_logout, name="logout"),
    
]