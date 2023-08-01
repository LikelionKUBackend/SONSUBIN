from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User

from pybo.models import Question, Answer
import requests
from .serializers import LoginSerializer,SignUpSerializer

from rest_framework import viewsets, views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LoginSerializer
from rest_framework.renderers import JSONRenderer
import json


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


@api_view(["POST"])
def LoginAPI(request):
    if request.method == "POST":
        userdata = request.data
        serializer = LoginSerializer(data = userdata)
        #login 정보에 대한 유효성 검사를 시행.
        #이때 serializers.py에 validate 함수 이름은 validate로 정해져 있어야함.
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            login(request, user)
        return Response(serializer.data)

@api_view(["POST"])
def SignUpAPI(request):
    if request.method == "POST":
        userdata = request.data

        '''
        username=userdata.get('username')
        raw_password=userdata.get('password')
        '''

        serializer = SignUpSerializer(data = userdata)
        if serializer.is_valid(raise_exception=True):
        #user = User.objects.create_user(username=username, password=raw_password)
        #user.set_password(raw_password)
        #login(request, user)
            return Response(serializer.data)