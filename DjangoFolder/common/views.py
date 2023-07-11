from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        raw_password = request.POST.get('password1')
    
        user = authenticate(username=username, password=raw_password)
        user = User.objects.create_user(username=username, password=raw_password)
        login(request, user)

        return redirect('pybo:index')
    return render(request, 'common/signup.html')