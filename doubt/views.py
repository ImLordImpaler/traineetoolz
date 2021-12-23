from django.shortcuts import render

def doubtIndex(request):
    return render(request , 'doubt/index.html')

def doubt(request):
    return render(request , 'doubt/doubt.html')