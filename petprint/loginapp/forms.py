from .models import NickName
from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username']
        

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "아이디"
        self.fields['password1'].label = "비밀번호"
        self.fields['password2'].label = "비밀번호 확인"
        
        self.fields['username'].widget.attrs.update(
            {'placeholder': '아이디',
             'class': "ac_item"})
        self.fields['password1'].widget.attrs.update(
            {'placeholder': '비밀번호',
             'class': "ac_item",
             'id': "password1"})
        self.fields['password2'].widget.attrs.update(
            {'placeholder': '비밀번호 확인',
             'class': "ac_item",
             'id': "password2"})     #이게 html 클래스 처럼 이름부여해주는거라서 나중에 회원가입 필드니까 css에서 클래스네임으로 바꿔주면됨
'''
class  NickNameForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(NickNameForm, self).__init__(*args, **kwargs)
        

        self.fields['nickname'].widget.attrs.update(
            {'placeholder': '닉네임',
            'class': "pf_name fo-rm",
            'id': "pf_name"}) #나중에 css할때 수정

    class Meta:
        model = NickName
        fields = [ 'nickname' ]
'''