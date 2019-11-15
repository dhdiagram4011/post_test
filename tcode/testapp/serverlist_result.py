from django.urls import path
from . import views

urlpatterns = [
    path('',views.serverlist_result, name='serverlist_result')
]