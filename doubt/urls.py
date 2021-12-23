from django.urls import path
from doubt import views
urlpatterns =[
    path('doubtIndex' , views.doubtIndex , name='dagueIndex'),
    path('doubt/<str:pk>' , views.doubt , name='doubt')
]