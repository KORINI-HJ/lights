from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User


from .models import Profile, Follow
from home.models import Diary

# Create your views here.
def profile(request, pet_id):
    context = {}
    try:
        followers = Follow.objects.filter(followee=pet_id)
        context['followers'] = followers

        list_followers = []
        for follower in followers:
            list_followers.append(follower.follower)
        context['list_followers'] = list_followers

        diary = Diary.objects.filter(owner_id=pet_id)
        context['diary'] = diary

        profile = Profile.objects.get(owner_id=pet_id)
        context['profile'] = profile
        
    except ObjectDoesNotExist:
        return redirect('profile_create', pet_id)

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

def follow(request, followee, follower):
    follow = Follow(follower_id=follower, followee_id=followee)
    follow.save()
    return redirect('profile', followee)

def unfollow(request, followee, follower):
    follow = Follow.objects.get(follower_id=follower, followee_id=followee)
    follow.delete()
    return redirect('profile', followee)