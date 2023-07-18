from django.urls import path
from . import views

app_name='pybo'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/form',views.question_form,name="question_form"),
    path('question/create', views.question_create, name='question_create'),
    path('question/modify/<int:question_id>',views.question_modify,name='question_modify'),
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
]
# config/urls.py 에서 건네 받고 그 뒤에 ""이면 views.py의 index를 실행해라!
# name 은 별칭!