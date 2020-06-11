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

from home.views import index, detail, comment_create, DiaryCreateView, DiaryUpdateView, DiaryDeleteView
from loginapp.views import sign_up,nickname
from django.contrib.auth.views import LoginView,LogoutView #sign_up기능은 장고에서 없어서 따로 view에서 함수 써주고 나머지 로그인,로그아웃은 장고에 있어서 따로 그냥 가져옴.
from userapp.views import ProfileView, profile_create

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('detail/<int:diary_id>', detail, name='detail'),
    path('create/', DiaryCreateView.as_view(), name='create'),
    path('<int:pk>/update/', DiaryUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', DiaryDeleteView.as_view(), name='delete'),
    path('comment_create/<int:diary_id>', comment_create, name='comment_create'),
    path('loginapp/sign_up/', sign_up, name="sign_up"),
    path('loginapp/login/',LoginView.as_view(),name="login"),
    path('loginapp/logout/',LogoutView.as_view(),name="logout"),
<<<<<<< HEAD
    path('userapp/profile/', profile, name="profile"),
    path('userapp/profile_edit/', profile_edit, name="profile_edit"),
    path('<int:pk>/<int:pk>/follow/', follow, name='follow'),
=======
    url(r'^profile_create/(?P<pk>[0-9]+)/$', ProfileView.as_view(), name='profile'),
    path('userapp/profile_create/', profile_create)
>>>>>>> 27b7bbd79df73a204315c93e80bd81de85c9cf3f
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

