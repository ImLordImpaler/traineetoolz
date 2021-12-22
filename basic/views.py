from django.shortcuts import render
from basic.models import Company , Question , Method , Difficulty , Type

from notes.models import Unit , Subject





def index(request):
    companies = Company.objects.all()
    types = Type.objects.all()
    subjects = Subject.objects.all()
    unit = Unit.objects.all()
    context = {
        'unit': unit,
        'subjects': subjects,
        'companies':companies,
        'types': types
    }
    return render(request , 'index.html', context)

def question_by_type(request, pk):
    ques = Question.objects.filter(typeOf = pk)
    context = {
        'ques':ques,
        'pk':pk
    }
    return render(request , 'question_by_type.html',context)

def question_detail(request, pk):
    ques = Question.objects.get(id=pk)
    methods = Method.objects.filter(question = ques)
    context = {
        'ques':ques,
        'methods': methods
    }
    return render(request , 'question_detail.html', context)