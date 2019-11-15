from django.urls import path
from . import views

urlpatterns = [
    path('', views.join_result, name='join_result'),
]
