"""petprint URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from .views import profile, ProfileUpdateView, ProfileCreateView, follow, unfollow

urlpatterns = [
    path('<int:user_id>/profile/', profile, name='profile'),
    path('<int:pk>/profile_create/', ProfileCreateView.as_view(), name='profile_create'),
    path('<int:pk>/profile_update/', ProfileUpdateView.as_view(), name='profile_update'),
    path('follow/<int:followee>/<int:follower>', follow, name='follow'),
    path('unfollow/<int:followee>/<int:follower>', unfollow, name='unfollow'),
]

