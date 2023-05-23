from django.http import HttpResponse

def index(request):
    return HttpResponse(Health())
# Create your views here.


def Health():
    str=""
    for i in range(1,4):
        str+="회원님~! %d 세트 시작하겠습니다!<br>" %i
        for j in range(1,11):
            str+="%d<br>" %j
    return str

# 웹브라우저 html로 띄우는거니까 개행문자를 <br>로 해줘야한다!