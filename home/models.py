from django.db import models
import uuid
from django.db.models.signals import pre_save
from django.db.models import Q
# Create your models here.


class Level(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    choices_dept = (('BEI', 'Electronics, communication and information engineering'), ('BCT', 'Computer Engineering'), ('BCE', 'Civil Engineering'),
                    ('BEL', 'Electrical Engineering'), ('BME', 'Mechanical Engineering'), ('BAM', 'Automobile Engineering'), ('BIE', 'Industrial Engineering'))
    department = models.CharField(max_length=100, choices=choices_dept)
    choices_sem = (('I', 'First'), ('II', 'Second'), ('III', 'Third'), ('IV', 'Fourth'),
                   ('V', 'Fifth'), ('VI', 'Sixth'), ('VII', 'Seventh'), ('VIII', 'Eighth'))
    semester = models.CharField(max_length=100, choices=choices_sem)

    def __str__(self):
        return str(self.department) + " " + str(self.semester)

    def save(self, *args, **kwargs):
        self.department = self.department.upper()
        self.semester = self.semester.upper()
        super().save(*args, **kwargs)


class Day(models.Model):
    week_days = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    day = models.CharField(max_length=100, choices=week_days)

    class Meta:
        # order with respect to day from monday to sunday
        ordering = ['day']
        unique_together = ('day',)

    def __str__(self):
        return str(self.day)


# class Category(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     category = models.CharField(max_length=100)

#     def __str__(self):
#         return str(self.category)


class Subject(models.Model):
    choices = (
        ('TH', 'Theory'),
        ('L', 'Lab'),

    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    subject = models.CharField(max_length=100)
    teacher = models.CharField(max_length=100, default="TBA")
    category = models.CharField(max_length=100, choices=choices)
    # if the lab choice is choosen then add the group field
    group = models.CharField(
        max_length=100, choices=(('A', 'A'), ('B', 'B'), ('Both', 'Both')), default='Both')
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return str(self.subject) + "(" + str(self.category) + ")" + " " + str(self.level) + " " + str(self.day) + " " + str(self.start_time) + " " + str(self.end_time)

    class Meta:
        ordering = ['-day']
        # unique together for class routine
        unique_together = ('level', 'day', 'category',
                           'start_time', 'end_time', 'group')

    def save(self, *args, **kwargs):
        self.teacher = self.teacher.upper()
        if self.start_time >= self.end_time:
            raise Exception("Start time cannot be greater than end time")
        if self.category == 'TH' and self.group != 'Both':
            self.group = 'Both'
            raise Exception(
                "Theory classes cannot have group A or B. It must be both")

        conflicting_routines = Subject.objects.filter(Q(
            day=self.day) & (Q(start_time__lt=self.end_time) & Q(end_time__gt=self.start_time)) & Q(group=self.group)).exclude(id=self.id)
        print(conflicting_routines)
        if conflicting_routines:
            raise Exception(
                "There is a conflict with another class routine")
        super(Subject, self).save(*args, **kwargs)
