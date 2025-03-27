from django.urls import path
from . import views

urlpatterns = [
    path('', views.shorter, name='shorter'),
    path('<short_code>/', views.redirecter, name='redirecter'),
    path('delete/<int:pk>', views.deleteUrl, name='deleteUrl')
]