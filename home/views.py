from django.shortcuts import render
from home.models import Subject, Level
from django.db.models import Q
from datetime import date
# Create your views here.


def home(request):
    date_today = date.today()
    day_today = date_today.strftime("%A")
    levels = Level.objects.all()
    days = Subject.objects.values('day__day').distinct()
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
            context = {'subjects': subjects,
                       'level': level, 'day': day, 'sem': sem}

        routine_today = Subject.objects.filter(
            Q(level__department="BEI") & Q(day__day=day_today) & Q(level__semester="II")).order_by('start_time')
        context['routine_today_subjects'] = routine_today
        context['levels'] = levels
        context['days'] = days

    return render(request, 'home/home.html', context=context)
