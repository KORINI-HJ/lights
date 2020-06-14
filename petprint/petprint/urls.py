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

from home.views import index, detail, comment_create, DiaryCreateView, DiaryUpdateView, DiaryDeleteView, follow_index, search_hashtag
from Profile.views import profile, ProfileUpdateView, ProfileCreateView, follow, unfollow

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('detail/<int:diary_id>', detail, name='detail'),
    path('create/', DiaryCreateView.as_view(), name='create'),
    path('<int:pk>/update/', DiaryUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', DiaryDeleteView.as_view(), name='delete'),
    path('comment_create/<int:diary_id>', comment_create, name='comment_create'),
    path('login/', include('loginapp.urls')),
    path('profile/', include('Profile.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('follower_index/<int:user_id>', follow_index, name='follow_index' ),
    path('tag/<int:tag_id>', search_hashtag, name='search_hashtag'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

