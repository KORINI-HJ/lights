from django.shortcuts import render

# Create your views here.
def profile(request):
    return render(request,'profile.html')

def profile_edit(request):
    return render(request,'profile_edit.html')