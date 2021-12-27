from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User , related_name='user_profile', on_delete=models.CASCADE)
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    age = models.IntegerField(default=18)
    designation = models.CharField(max_length=255)

    image = models.ImageField(upload_to='profile/')

    def __str__(self):
        return self.user.username


@receiver(post_save, sender = User)
def create_profile(sender , instance , created , **kwargs):
    if created:
        profile = Profile.objects.create(user=instance )
        profile.save()