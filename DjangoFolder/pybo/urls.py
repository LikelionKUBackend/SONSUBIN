from django.urls import path
from . import views

app_name='pybo'

urlpatterns = [
    path('', views.index),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
]
# config/urls.py 에서 건네 받고 그 뒤에 ""이면 views.py의 index를 실행해라!
# name 은 별칭!