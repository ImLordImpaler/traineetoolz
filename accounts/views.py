from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login, logout
from django.http import HttpResponse

def register(request):
    return render(request, 'accounts/register.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        user = authenticate(request , username=username, password=pwd)
        if user is not None:
            login(request , user)
            return redirect('index')
        else:
            return HttpResponse('Kon hai bai?')
    return render(request, 'accounts/signin.html')

def signout(request):
    logout(request)
    return redirect('signin')