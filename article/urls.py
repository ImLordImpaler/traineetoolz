from django.urls import path
from . import views

urlpatterns = [
    path('article/<str:pk>' , views.index , name='articleIndex'),
    path('allArticles' , views.articleList, name='allArticles'),
    path('newArticle' , views.newArticle, name='newArticle'),
    path('preview/<str:pk>' , views.preview, name='preview'),
]