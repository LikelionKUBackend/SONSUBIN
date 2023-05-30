from django.shortcuts import render
from .models import Question

def index(request):
    question_list=Question.objects.order_by('-create_date')
    context={'question_list':question_list}
    return render(request,'pybo/question_list.html',context)
# Create your views here.


def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)
    
# 웹브라우저 html로 띄우는거니까 개행문자를 <br>로 해줘야한다!