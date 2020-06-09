from .models import Profile
from django import forms
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        

        self.fields['name'].widget.attrs.update(
            {'placeholder': '성명',
            'class': "pf_name fo-rm",
             'id': "pf_name"})

        self.fields['major'].widget.attrs.update(
            {'placeholder': '학과',
            'class':'fo-rm',
             'id': "pf_major"})

        self.fields['phone_number'].widget.attrs.update(
            {'placeholder': '010-0000-0000',
             'class': "pf_phone_number fo-rm",
             'id': "pf_phone_number"})

        self.fields['email'].widget.attrs.update(
            {'placeholder': '이메일',
            'class':'fo-rm',
             'id': "pf_email"})

        self.fields['m_or_f'].widget.attrs.update(
            {'placeholder': '성별',
            'class':'fo-rm',
             'id': "pf_m_or_f",})