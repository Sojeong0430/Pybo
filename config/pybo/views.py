from django.shortcuts import render , get_object_or_404, redirect
from .models import Question
from django.utils import timezone
from .forms import QuestionForm

# Create your views here.

def index(request):
    question_list = Question.objects.order_by('-create_date') #Question 모델의 모든 객체를 가져오되,최신 순으로 정렬된 목록을 변수에 저장
    context = {'list':question_list}#context라는 딕셔너리 생성/ 키:값/이를 통해 템플릿에 데이터를 전달
    return render(request,'pybo/question_list.html',context) #render함수 호출/ request:요청객체전달 / context는 템플릿에 전달할 데이터 
#데이터베이스에서 질문 목록을 가져와서 정렬한 후, 이 데이터를 템플릿에 전달하여 HTML페이지로 렌더링.
#이를 통해 사용자는 최신 질문 목록을 볼 수 있다.

def detail(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question':question}
    return render(request,'pybo/question_detail.html',context)
#question = Question.object.get(id='question_id')
#get 메서드는 주어진 조건에 맞는 객체를 하나만 반환한다. 여기서는 'id'필드가 'question_id'인 Question객체 하나만 반환한다.

def answer_create(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'),create_date=timezone.now())
    return redirect('pybo:detail',question_id=question.id)#^ 등록한 답변 내용은 request객체를 통해 읽을 수 있다.
#answer_set을 통해 특정 Question객체와 연결된 모든 Answer객체에 접근할수있다.
#.create()매서드는 새로운 Answer 객체를 생성하고 DB에 저장한다
#필요한 '필드 값'을 인자로 받아서 자동으로 '객체'를 생성하고 저장한다 
#redirect 함수는 페이지 이동을 위한 함수이다.

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST) #사용자가 제출한 폼데이터를 포함한다
        if form.is_valid(): #폼이 유효하다면(유효성 검사를 통과했다면)
            question = form.save(commit=False) #임시저장하여 question객체를 리턴받는다
            question.create_date = timezone.now() #실제저장을 위해 작성일시를 설정한다
            question.save() #데이터를 데이터베이스에 실제로 저장한다
            return redirect('pybo:index')
    else: #GET방식일때
        form = QuestionForm()
        context = {'form':form}
        return render(request,'pybo/question_form.html',context)
#form 태그에서 action속성을 지정하지 않았기 때문에 현재 페이지가 디폴트로 action된다
#따라서 POST 방식으로 요청된다.
#GET방식일때는 QuestionForm을 인수없이 생성했지만,
#POST방식에서는 request.POST를 인수로 생성했다.
#request.POST에는 화면에 사용자가 입력한 내용들이 담겨있다.

