from django.shortcuts import render , redirect
from article.models import Article, Reaction
from article.forms import ArticleForm

def index(request ,pk):
    article = Article.objects.get(id=pk)
    params = {'article': article}
    return render(request, 'article/index.html', params)


def articleList(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'article/list.html' , context)

def newArticle(request):
    
    if request.method == 'POST':
        title = request.POST.get('title')
        subject = request.POST.get('subject')
        body = request.POST.get('body')
        img = request.FILES.get('img')
        article = Article.objects.create(user=request.user, title=title, subject=subject, body=body , image = img)
        article.save()
        # form = ArticleForm(request.POST , request.FILES)
        # if form.is_valid():
        #     form.save()
        return redirect('preview', pk=article.id)
    else:
        form = ArticleForm()
    context = {'form': form}
    return render(request , 'article/newArticle.html', context)

def preview(request , pk):
    article = Article.objects.get(id=pk)
    context = {'article': article}
    return render(request , 'article/preview.html' , context)