from django.shortcuts import render,redirect #render는 그냥 템플릿에 있는 html을 띄워주는 역할,redirect는 해당 url로 url요청을 다시 보내주는 것이다.
from django.contrib.auth.forms import UserCreationForm  #장고에서 기본적으로 제공해주는 UserCreationForm을 사용합니다
#기본적으로 만들어져있는 User모델에서 User생성을 쉽게 도와주는 모델폼으로 생각합시다.

# Create your views here.
def index(request):
    return render(request,'index.html')

def sign_up(request):
    if request.method == 'POST':
        registerform = RegisterForm(request.POST)
        if registerform.is_valid():
            user_instance = registerform.save(commit=False)
            user_instance.set_password(registerform.cleaned_data['password1'])
            user_instance.is_active = True
            user_instance.save()
            user=User.objects.get(username=registerform.cleaned_data['username'])
            auth.login(request, user,
                       backend='django.contrib.auth.backends.ModelBackend')
            return redirect('nickname')
        else:
            registerform = RegisterForm(request.POST)
            return render(request, 'registration/sign_up.html', {'RegisterForm': registerform})

    registerform = RegisterForm()
    return render(request, 'registration/sign_up.html',{'RegisterForm':registerform})

def nickname(request):
    user = request.user
    nickname = user.nickname
    
    nicknameform = NickNameForm(request.POST or None, request.FILES, instance=nickname)

    context = {'NickNameform':nicknameform,
                    'NickName':nickname}

    if request.method == 'POST':
        if nicknameform.is_valid():
            nickname.save()  
            return redirect('index')
        
        else:
            return render(request, 'registration/nickname.html', context)

            
    nicknameform = NickNameForm(instance=nickname)
    context = {'NickNameform':nicknameform,
                    'NickName':nickname}
    

    return render(request, 'registration/nickname.html', context)

