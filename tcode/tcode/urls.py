"""tcode URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('join/', include('testapp.join')),
    path('join_result/', include('testapp.join_result')),
    path('translate/', include('testapp.translate')), 
    path('translate_result/' , include('testapp.translate_result')),
    path('serverlist/', include('testapp.serverlist')),
    path('serverlist_result/', include('testapp.serverlist_result')),
    path('', include('testapp.main')),
    path('login/' , include('testapp.login')),  
    path('login_success/' , include('testapp.login_success')), 
    path('logout/' , include('testapp.logout')),
]


