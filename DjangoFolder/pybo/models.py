from django.db import models
# Create your models here.

class Question(models.Model):
    subject = models.CharField(max_length = 200)
    content = models.TextField()
    create_date = models.DateTimeField()

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    # 외부의 키인데, Question이라는 모델에 있다!
    # on_delete(삭제가 되면)->CASCADE로(종속된 질문이 삭제되면 그 질문을 foreign key로 가지는 애들을 전부 삭제하는!)
    content = models.TextField()
    create_date = models.DateTimeField()
