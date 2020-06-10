from django import forms
from .models import Profile
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        
        self.fields['name'].widget.attrs.update(
            {'placeholder': '닉네임',
            'class': "pf_name fo-rm",
             'id': "pf_name"})

        self.fields['image'].widget.attrs.update(
            {'placeholder': '이미지',
            'class':'fo-rm',
             'id': "pf_major"})
    
    class Meta:
        model = Profile
        fields = '__all__'