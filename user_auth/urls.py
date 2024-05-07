from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from EventApp import settings

app_name = 'user_auth'

urlpatterns = [
    path('login', views.user_login, name='user_login'),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='user_logout',)
]
