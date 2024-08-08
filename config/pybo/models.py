from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    #null=True는 데이터베이스에서 modify_date칼럼에 null을 허용한다는 의미이다
    #blank=True는 form.is_valid()를 통한 데이터 검증 시 값이 없어도 된다는 의미이다.
    #즉,위 두가지는 어떤 조건으로든 값을 비워둘 수 있음을 의미한다.
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='author_question')
    voter = models.ManyToManyField(User,related_name='voter_question')

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='auhtor_answer')
    voter = models.ManyToManyField(User,related_name='voter_answer')
    #ManyToMany는 두 모델 간의 다대다 관계를 정의하는데 사용된다.

#쿼리는 데이터 베이스에서 데이터를 검색하거나 조작하기 위해 작성되는 명령문이다