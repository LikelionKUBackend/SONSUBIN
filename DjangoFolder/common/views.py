from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from pybo.models import Question, Answer


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        raw_password = request.POST.get('password1')
    
        user = authenticate(username=username, password=raw_password)
        user = User.objects.create_user(username=username, password=raw_password)
        login(request, user)

        return redirect('pybo:index')
    return render(request, 'common/signup.html')

def mypage(request):
    myquestion_list=Question.objects.filter(author = request.user)
    context = {'myquestion_list': myquestion_list}
    return render(request, 'common/mypage.html',context)