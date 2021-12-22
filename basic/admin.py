from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Question)
admin.site.register(Method)
admin.site.register(Company)
admin.site.register(Difficulty)
admin.site.register(Type)