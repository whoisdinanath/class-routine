
from django.urls import path
from .views import home, RoutineClassView, RoutineTeacherView

urlpatterns = [
    path('', home, name='home'),
    path('routine/class/', RoutineClassView, name='routine'),
    path('routine/teacher/', RoutineTeacherView, name='routine'),

]
