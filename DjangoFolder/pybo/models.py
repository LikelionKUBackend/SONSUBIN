from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Question(models.Model):
    subject = models.CharField(max_length = 200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #User 모델에 있는 Foreign Key
    content = models.TextField()
    create_date = models.DateTimeField()
    def __str__(self):
        return self.subject
        # python 에서 __ __ 는 내장함수를 뜻함.
        # str은 Question을 불렀을때, 반환값을 지정해주는 것.
        # default로는 id값을 반환한다.
    


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # on_delete(삭제가 되면)->CASCADE로(종속된 질문이 삭제되면 그 질문을 foreign key로 가지는 애들을 전부 삭제하는!)
    # Foreign Key: 외부의 키인데, Question이라는 모델에 있다!
    # 각 객체의 Foreign key 필드는 참조하고 있는 모델의 객체를 넣어줘야한다!
    # 즉, Answer객체는 Question에 종속되어있다.!
    content = models.TextField()
    create_date = models.DateTimeField()


