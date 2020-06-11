from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.urls import reverse_lazy

from .models import Profile
from home.models import Diary

# Create your views here.
def profile(request, user_id):
    context = {}
    
    profile = Profile.objects.get(owner_id=user_id)
    context['profile'] = profile


    diary = Diary.objects.filter(owner_id=user_id)
    context['diary'] = diary
    return render(request, 'profile.html', context)

class OwnerOnlyMixin(AccessMixin):
    raise_exception = True
    permission_denied_message = 'Owner only can update the profile'

class ProfileCreateView(OwnerOnlyMixin, CreateView):
    model = Profile
    fields = ['pet_name', 'pet_image', 'pet_explain']
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ProfileUpdateView(OwnerOnlyMixin, UpdateView):
    model = Profile
    fields = ['pet_name', 'pet_image', 'pet_explain']
    success_url = reverse_lazy('index')