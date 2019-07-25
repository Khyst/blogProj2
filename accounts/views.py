from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# 예외 상황 나중에 구현
@csrf_exempt
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                request.POST['username'], password = request.POST['password1']
            )
            auth.login(request, user)
            return redirect('')
    return render(request, 'accounts/signup.html')

#예외 상황도 구현
@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        user = auth.authenticate(request, username=username)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accuonts/login.html')
    return render(request, 'accounts/login.html')

@csrf_exempt
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('blog')
    return render(request, 'accounts/signup.html')

    
