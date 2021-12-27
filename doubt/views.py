from django.shortcuts import render , redirect
from doubt.models import Doubt , Response , Tag

def doubtIndex(request):
    return render(request , 'doubt/index.html')

def doubt(request, pk):
    doubt = Doubt.objects.get(id=pk)
    if request.method == 'POST':
        response = request.POST.get('response')
        temp = Response.objects.create(user=request.user , doubt = doubt, answer = response)
        temp.save()
        doubt.responses.add(temp)
        doubt.save()
        return redirect('doubt', pk=doubt.id)

    context = {
        'doubt': doubt
    }
    return render(request , 'doubt/doubt.html', context)

def newDoubt(request):
    tags = Tag.objects.all()
    if request.method == 'POST':
        ques = request.POST.get('ques')
        body = request.POST.get('body')
        tags = request.POST.getlist('tags')
        doubt = Doubt.objects.create(user=request.user,ques=ques, body=body )
        for i in tags:
            doubt.tags.add(i)
        doubt.save()
        return redirect('doubt', pk=doubt.id)
    context = {
        'tags': tags,
    }
    return render(request , 'doubt/newDoubt.html', context)