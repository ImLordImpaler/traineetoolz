from django.urls import path, include
from basic import views
urlpatterns = [
    path('', views.index , name='index'),


    path('question_by_type/<str:pk>' , views.question_by_type , name='question_by_type'),

    path('question_detail/<str:pk>', views.question_detail , name='question_detail')
]