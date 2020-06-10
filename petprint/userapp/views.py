from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import AccessMixin
from django.urls import reverse_lazy
from .models import Profile
from .forms import ProfileForm

# Create your views here.
'''
def profile_edit(request):
    return render(request,'profile_edit.html')
'''
def profile(request):
    return render(request, 'profile.html')

class OwnerOnlyMixin(AccessMixin):
    raise_exception = True
    permission_denied_message = "Owner only can update/delete the object다."

class ProfileView(OwnerOnlyMixin, CreateView):
    model = Profile
    fields = ['name', 'images']
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)