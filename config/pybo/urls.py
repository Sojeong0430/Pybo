from django.urls import path
from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.index,name='index'),
    path('<int:question_id>/',views.detail,name='detail'),
    #http://localhost:8000/pybo/2/ (2는 아이디값) 가 요청되면 , <int:question_id> 매핑 룰에 의해
    # http://localhost:8000/pybo/<int:question_id>/ 가 적용되어
    #question_id에 2가 저장되고 detail뷰가 실행된다.
    path('answer/create/<int:question_id>/',views.answer_create,name='answer_create'),
    path('question/create/',views.question_create,name='question_create'),
]