from django.urls import path
from doubt import views
urlpatterns =[
    path('doubtIndex' , views.doubtIndex , name='doubtIndex'),
    path('doubt/<str:pk>' , views.doubt , name='doubt'),
    path('newDoubt', views.newDoubt , name='newDoubt')
]