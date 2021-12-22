from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE , null=True, blank=True) 
    f_name = models.CharField(max_length=1000)
    m_name = models.CharField(max_length=1000 , null=True, blank=True)
    l_name = models.CharField(max_length=1000)

    designation = models.CharField(max_length=1000)

    skills = models.CharField(max_length=100) #Change to manytomany


    profile_picture = models.ImageField(null=True, blank=True)
    friends = models.ManyToManyField('Profile' , blank=True)

    def __str__(self):
        if self.m_name:
            return str(self.f_name + ' ' + self.m_name + ' ' + self.l_name)
        else:
            return str(self.f_name + ' ' + self.l_name )


class Post(models.Model):
    text = models.CharField(max_length=1000)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True , null=True, blank=True) 
    def __str__(self):
        return str(self.text+ ' - ' + self.user.username)

class Comment(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    def __str__(self):
        return str(self.text+' - '+ self.user.username)
