from django.shortcuts import render,redirect #render는 그냥 템플릿에 있는 html을 띄워주는 역할,redirect는 해당 url로 url요청을 다시 보내주는 것이다.
from django.contrib.auth.forms import UserCreationForm  #장고에서 기본적으로 제공해주는 UserCreationForm을 사용합니다
#기본적으로 만들어져있는 User모델에서 User생성을 쉽게 도와주는 모델폼으로 생각합시다.

# Create your views here.
def index(request):
    return render(request,'index.html')

def sign_up(request):

    if request.method =="POST":      #data 수정행위- 보안 -POST -해당if절 실행  

        # signup폼을 그냥 생성하는게 아닌 request.POST로 넘어가는 DATA들 즉, 우리가 입력한 ID와 PW를 넣어서 객체를 생성합니다                                       

        sign_up_form = UserCreationForm(request.POST) 

        if sign_up_form.is_valid():                     #그리고 해당 form의 요구대로 유효한 값이 입력이 되었으면
            sign_up_form.save()                       #데이터를 받은 폼 객체를 저장해주고
            return redirect('index')                  #index라는 애칭의 url요청을 redirect해줍니다.

        else:                                         #유효성 검사가 실패하게 되면

            return redirect('sign_up')                #다시금 sign_up url요청을 보내 페이지를 다시 리로드 해줍니다.

    sign_up_form = UserCreationForm()  
    #우리가 href link를 누르는 행위는 기본적으로 request get요청을 보냅니다. 따라서 get요청이 들어왔을때는
    #UserCreationForm을 빈 form으로 sign_up_form이라는 유저 생성 폼을 만들어 줍니다.

    return render(request,'registration/sign_up.html', {'sign_up_form':sign_up_form})  #그리고 우리는 유저생성폼을 전달해서 template에 띄워줍니다.
    #LoginView의 login.html과 같은 기능을 하는 template이므로 같은 폴더에 넣어주기 위해 LoginView의 login.html이 위치하는 폴더 밑에 미리 위치