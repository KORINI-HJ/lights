from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.urls import reverse_lazy

from .models import Profile, Follow
from home.models import Diary

# Create your views here.
def profile(request, owner_id):
    context = {}
    print('start')
    try:
        followers = Follow.objects.filter(followee=owner_id)
        context['followers'] = followers
        print('followers: ', followers)

        list_followers = []
        for follower in followers:
            list_followers.append(follower.follower)
        context['list_followers'] = list_followers
        print('list: ', list_followers)
        
        diary = Diary.objects.filter(owner_id=owner_id)
        context['diary'] = diary
        print('diary: ', diary)

        profile = Profile.objects.get(owner_id=owner_id)
        context['profile'] = profile
        print(profile)
        
    except:
        pass

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