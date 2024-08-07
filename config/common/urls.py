from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='common/login.html'),name='login'),
    #로그인 뷰는 따로 만들필요 없이 위 코드처럼 django.contrib.auth앱의
    #LoginView를 사용하도록 설정했다.
    path('logout/',views.logout_view,name='logout'),
    path('signup/',views.signup, name='signup'),
    ] 