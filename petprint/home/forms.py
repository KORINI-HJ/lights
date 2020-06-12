from django import forms
from .models import Diary, Comment
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class DiaryForm(forms.ModelForm):
    
    # 메타 클래스란 클래스 안에 선언해서 상위의 클래스에게 메타데이터, 즉 옵션이나 데이터를 추가해줄 수 있는 것
    class Meta:
        model = Diary
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)



class CreateDiary(forms.ModelForm):
    class Meta:
        model = Diary

        fields = ['title', 'body']

        widgets = {
                    'title': forms.TextInput(
                        attrs={'class': 'form-control', 'style': 'width: 100%', 'placeholder': '제목을 입력하세요.'}
                    ),
                    'body': forms.CharField(widget=CKEditorUploadingWidget()),
                }