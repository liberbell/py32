from django.urls import path
from . import views
from users import views as user_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="index"),
    path('business', views.business, name='business'),
    path('register/', user_view.register, name='register'),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
]