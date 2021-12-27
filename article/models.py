from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=1000)
    body =  models.TextField()
    isApproved = models.BooleanField(default=False)
    reactions = models.ManyToManyField('Reaction' , related_name='article_reaction' , blank=True)
    image = models.ImageField(upload_to="images/",null=True, blank=True)
    #tags
    published = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.username + " - "+ self.title)

class Reaction(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    #find better way to map rating
    rating = models.IntegerField(default=0)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.user.username + " - " + str(self.rating))