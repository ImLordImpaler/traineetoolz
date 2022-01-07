from django.urls import path, include
from basic import views
urlpatterns = [
    path('', views.index , name='index'),


    path('question_type/<str:pk>' , views.question_by_type , name='question_by_type'),
    path('question_diff/<str:pk>' , views.question_diff , name='question_diff'),
    path('question_detail/<str:pk>', views.question_detail , name='question_detail')
]