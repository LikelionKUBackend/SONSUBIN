from django.shortcuts import render
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest

# Create your views here.

def calculator(request):
    #return HttpResponse("계산기 기능 구현 시작합니다^^")
    
    # 1. 데이터 확인
    num1=request.GET.get('num1')
    num2=request.GET.get('num2')
    operators = request.GET.get('operators')

    # 2. 계산
    if operators =='+':
        result = int(num1)+int(num2)
    elif operators =='-':
        result = int(num1)-int(num2)
    elif operators =='*':
        result = int(num1)*int(num2)
    elif operators =='/':
        result = int(num1)/int(num2)
    else:
        result=0

    # 3. 응답
    return render(request, 'calculator.html',{'result':result})
    #result라는 key에 result 값을 넘겨줌