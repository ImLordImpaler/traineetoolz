from django.shortcuts import render, redirect
from feed.models import *

def index(request):
    posts = Post.objects.all().order_by('-date')

    if request.method == 'POST':
        data = request.POST.get('data')
        Post.objects.create(text=data, user = request.user)
        return redirect('feed')
    context = {
        'posts':posts
    }
    return render(request, 'feed/feed.html' , context)

