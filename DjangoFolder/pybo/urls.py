from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:question_id>/', views.detail),
]
# config/urls.py 에서 건네 받고 그 뒤에 ""이면 views.py의 index를 실행해라!