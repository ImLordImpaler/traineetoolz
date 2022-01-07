from django.shortcuts import render
from basic.models import Company , Question , Method , Difficulty , Type

from notes.models import Unit , Subject
from article.models import Article
from doubt.models import Doubt
from django.contrib.auth.decorators import login_required


@login_required(login_url="signin")
def index(request):
    difficulty = Difficulty.objects.all()
    companies = Company.objects.all()
    types = Type.objects.all()
    subjects = Subject.objects.all()
    unit = Unit.objects.all()
    articles = Article.objects.filter(published=True)
    doubts = Doubt.objects.all()
    

    # easy=0
    # mid = 0
    # hard =0

    # questions = Question.objects.all()
    # for i in questions:
        
    #     if i.difficulty.id == 1:
    #         easy +=1
    #     elif i.difficulty.id == 2:
    #         mid +=1
    #     elif i.difficulty.id == 3:
    #         hard +=1
    
    context = {
        'articles': articles,
        'unit': unit,
        'subjects': subjects,
        'companies':companies,
        'types': types,
        'doubts':doubts,
        'difficulty':difficulty
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

def question_diff(request, pk):

    context = {}
    return render(request , 'question_diff.html', context)