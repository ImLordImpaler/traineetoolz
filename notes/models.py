from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=1000)
    img = models.ImageField(null=True , blank=True)
    def __str__(self):
        return self.name


class Unit(models.Model):
    number = models.IntegerField()
    pdf = models.FileField()
    subject = models.ForeignKey(Subject, blank=True , on_delete=models.CASCADE)

    def __str__(self):
        return str(self.subject.name + ' - ' + str(self.number))
    
