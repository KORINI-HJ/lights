from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from django.views import View
from .forms import ProfileForm
# Create your views here.


class ProfileView(DetailView):
    context_object_name = 'profile_user'
    model = User
    template_name = 'profile_create.html'

def profile_create(request):
    return render(request, 'profile_create.html')