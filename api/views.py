from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Subject
from .serializer import SubjectSerializer
# import Q lookup
from django.db.models import Q
# Create your views here.


def home(request):
    return render(request, 'api/home.html')


@api_view(['GET'])
def RoutineClassView(request):
    if (request.method == 'GET'):
        if request.GET != None:
            level = request.GET.get('level')
            sem = request.GET.get('semester')
            day = request.GET.get('day')
            if (level and day and sem):
                subjects = Subject.objects.filter(
                    Q(level__department=level.upper()) & Q(day__day=day.capitalize()) & Q(level__semester=sem.upper())).order_by('start_time')
                serializer = SubjectSerializer(subjects, many=True)
            else:
                return Response("Invalid Query")
            return Response(serializer.data)


@api_view(['GET'])
def RoutineTeacherView(request):
    if (request.method == 'GET'):
        if request.GET != None:
            teacher = request.GET.get('teacher')
            level = request.GET.get('level')
            day = request.GET.get('day')
            sem = request.GET.get('semester')
            if (teacher and level and day and sem):
                subjects = Subject.objects.filter(
                    Q(teacher__iexact=teacher.uper()) & Q(level__department=level.upper()) & Q(day__day=day.capitalize()) & Q(level__semester=sem.upper())).order_by('start_time')
                serializer = SubjectSerializer(subjects, many=True)
            elif (teacher and level and sem):
                subjects = Subject.objects.filter(
                    Q(teacher__iexact=teacher.upper()) & Q(level__department=level.upper()) & Q(level__semester=sem.upper())).order_by('start_time')
                serializer = SubjectSerializer(subjects, many=True)
            else:
                return Response("Invalid Query")
            return Response(serializer.data)
