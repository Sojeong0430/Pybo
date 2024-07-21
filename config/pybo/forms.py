from django import forms
from pybo.models import Question , Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question #사용할 모델
        fields = ['subject','content'] #QuestionForm에서 사용할 Question필드

        labels={
        'subject' : '제목',
        'content' : '내용',}
        #질문 등록 화면에 표시되는 'Subject', 'Content'를
        # #한글로 표시하고 싶다면 위처럼 labels 속성을 지정하면 된다.

#QuestionForm은 모델 폼(forms.ModelForm)을 상속했다. 
#장고의 폼은 일반 폼(forms.Form)과 모델 폼(forms.ModelForm)이 있는데,
#모델 폼은 모델(Model)과 연결된 폼으로 폼을 저장하면,
#연결된 모델의 데이터를 저장할수 있는 폼이다.
#모델 폼은 이너 클래스인 Meta 클래스가 반드시 필요하다.
#Meta 클래스에는 사용할 모델과 모델의 속성을 적어야 한다.