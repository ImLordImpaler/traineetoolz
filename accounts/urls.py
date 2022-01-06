from django.urls import path
from accounts import views
urlpatterns = [
    path('register', views.register , name='register'),
    path('signin', views.signin , name='signin'),
    path('signout' , views.signout , name='signout'),
    path('profile/<str:pk>', views.profile , name='profile'),
]