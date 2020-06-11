from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Follow
# Create your views here.

@login_required
def follow(request, follower_id, followee_id):
    if request.method == 'POST':
        follow = Follow(followee=followee_id, follower=follower_id)
        follow.save()
    return render(request, 'index')