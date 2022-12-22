from django.contrib import admin
from .models import Level, Day, Subject
# Register your models here.
admin.site.register(Level)
admin.site.register(Day)
# admin.site.register(Category)
# admin.site.register(Subject)


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject', 'teacher', 'level', 'day',
                    'category', 'group', 'start_time', 'end_time')
    ordering = ['level', '-day', 'start_time']


admin.site.register(Subject, SubjectAdmin)
