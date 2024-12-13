from django.urls import path
from .views import logout_view, login_view, create_user

urlpatterns = [
    path('register/', create_user, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
