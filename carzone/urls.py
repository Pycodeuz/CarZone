from django.urls import path, include

from carzone import views

urlpatterns = [
    path('', views.home, name='home')
]