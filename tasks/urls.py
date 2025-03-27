from django.urls import path
from django.contrib.auth import views as av
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('complete/<int:pk>', views.complete, name='complete'),
    path('login/', av.LoginView.as_view(template_name='tasks/login.html'), name='login'),
    path('logout/', av.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),


]