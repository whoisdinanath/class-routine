from django.shortcuts import render
from api.models import Subject
from django.db.models import Q
# Create your views here.


def home(request):
    if request.method == 'GET':
        level = request.GET.get('level')
        sem = request.GET.get('semester')
        day = request.GET.get('day')
        context = {}
        if level != None and day != None and sem != None:
            level = level.upper()
            day = day.capitalize()
            sem = sem.upper()
            subjects = Subject.objects.filter(
                Q(level__department=level) & Q(day__day=day) & Q(level__semester=sem)).order_by('start_time')
            context = {'subjects': subjects}
    return render(request, 'home/home.html', context=context)
