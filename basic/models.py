from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.name

class Method(models.Model):
    name = models.CharField(max_length=100)
    space = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    question = models.ForeignKey('Question' ,blank=True,null=True, on_delete=models.CASCADE , related_name='questions_method')
    statement = models.TextField(blank=True)
    algo = models.ImageField(null=True , blank=True)
    code = models.ImageField(null=True, blank=True)
# TYPE_CHOICES = (
#     ('String' , 'String'),
#     ('Array' , 'Array'),
#     ('Linked List' , 'Linked List'),  
# )
# DIFFICULTY_CHOICES = (
#     ('Easy', 'Easy'),
#     ('Medium', 'Medium'),
#     ('Hard', 'Hard'),
# )

class Type(models.Model):
    string = models.CharField(max_length=1000)
    img = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.string


class Difficulty(models.Model):
    string = models.CharField(max_length=100)
    img = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.string
class Question(models.Model):
    ques = models.CharField(max_length=1000)
    first_statement = models.TextField(blank=True)
    methods = models.ManyToManyField(Method , blank=True , related_name='questions_methods')
    company = models.ManyToManyField(Company , blank=True)
    # typeOf = models.CharField(max_length=100 , choices=TYPE_CHOICES)
    typeOf = models.ForeignKey(Type , blank=True , null=True, on_delete=models.CASCADE)
    # difficulty = models.CharField(max_length=100 , choices=DIFFICULTY_CHOICES)
    difficulty = models.ForeignKey(Difficulty , blank=True , null=True, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.ques


