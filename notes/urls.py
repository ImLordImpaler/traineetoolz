from django.urls import path
from notes import views

urlpatterns = [
    path('subject-detail/<str:pk>' , views.SubjectDetail , name='subject-detail')
]