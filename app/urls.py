from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('blog/<int:id>/', views.blog, name='Blog'),
    path('login', views.loginV, name='Login'),
    path('logout', views.logoutV, name='Logout'),
    path('register', views.registerV, name='Register'),
]