from django.shortcuts import render
from article.models import Article, Reaction

def index(request ,pk):
    article = Article.objects.get(id=pk)
    params = {'article': article}
    return render(request, 'article/index.html', params)


def articleList(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'article/list.html' , context)