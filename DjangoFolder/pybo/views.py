from django.contrib.auth.models import User

from django.http import HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question, Answer

from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework.views import APIView
from .serializers import QuestionSerializer
from rest_framework.renderers import JSONRenderer

def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answer_list = Answer.objects.filter(question_id = question_id)
    context = {'question': question, 'answer_list': answer_list}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    author=request.user
    answer = Answer(author=author,question=question, content=request.POST.get('content'), create_date=timezone.now())
    answer.save()
    return redirect('pybo:detail', question_id=question.id)

def question_form(request):
    return render(request,'pybo/question_form.html')

def question_create(request):
    author=request.user
    question = Question(author=author,subject = request.POST.get('subject'), content=request.POST.get('content'), create_date=timezone.now())
    question.modify_date=question.create_date

    if question.subject=="":
        question.subject="제목없음"
    if question.content=="":
        question.subject="내용없음"
    
    question.save()
    return redirect('pybo:index')

def question_modify(request, question_id):
    question=get_object_or_404(Question, pk=question_id)
    if request.method=="POST":
        question.subject=request.POST.get('subject')
        question.content=request.POST.get('content')
        question.modify_date=timezone.now()
        question.save()
        return redirect('pybo:index')
    else:
        context={'question':question}
        return render(request,'pybo/question_modify_form.html',context)

def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.delete()
    return redirect('pybo:index')

def question_stars(request,question_id):
    question=get_object_or_404(Question, pk=question_id)

    #작업을 요청한 사용자가 이미 즐겨찾기 명단에 있다면 즐겨찾기 해제
    if request.user in question.star.all():
        question.star.remove(request.user)
        question.save()
    else:
        question.star.add(request.user)
        question.save()
    return redirect('pybo:detail',question_id=question.id)

def apiTest(request):
    author = request.user
    author_list = serializers.serialize('json', author) 
    return HttpResponse(author_list, content_type='text/')


@api_view(["GET","POST"])
def QuestionListAPI(request):
    queryset = Question.objects.all()
    print(queryset)
    serializer = QuestionSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(["GET", "POST"])
def create_question_by_api(request):
    print(request.data)
    author = User.objects.get(pk = 1, is_superuser=True)
    question = Question(author = author, subject = request.data.get('subject'), content=request.data.get('content'), create_date=timezone.now())
    question.modify_date = question.create_date
    question.save()
    return redirect('pybo:index')