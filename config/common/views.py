from django.shortcuts import render , redirect
from django.contrib.auth import logout , authenticate , login
from common.forms import UserForm

def logout_view(request):
    logout(request)
    return redirect('index')
#로그아웃 함수에 요청 request객체만 인자로 전달해주면 로그아웃이 끝난다

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save() #데이터베이스에저장
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username , password=raw_password) #사용자인증
            login(request,user) #로그인
            return redirect('index')
    else:
        form = UserForm()
        return render(request,'common/signup.html',{'form':form})

#form.cleaned_data:데이터가 유효성 검사를 통과한 후 각 필드의 값을 딕셔너리 형태로 저장하는 속성
#authenticate() : 사용자 자격 증명 확인