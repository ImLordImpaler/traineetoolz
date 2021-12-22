from django.shortcuts import render
from notes.models import Unit , Subject


def SubjectDetail(request, pk):
    units = Unit.objects.filter(subject = pk)
    context = {
        'unit':units
    }
    return render(request, 'notes/subject-detail.html' , context)