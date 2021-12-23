from django.db import models
from django.contrib.auth.models import User
class Doubt(models.Model):
    ques = models.CharField(max_length=1000)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    #tags 
    body = models.TextField(null=True, blank=True)

    responses = models.ManyToManyField('Response' ,related_name='doubt_response', blank=True)

    def __str__(self):
        return self.ques

class Response(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    answer = models.TextField()
    approve = models.BooleanField(default=False)
    doubt = models.ForeignKey(Doubt, on_delete=models.CASCADE)
    def __str__(self):
        return self.answer
