from pyexpat import model
from statistics import mode
from django.utils.timezone import now
from django.db import models

# Create your models here.


# Announcements from CRs and Admins
class announcements(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True) 
    created_at = models.DateField(default=now)

    def __str__(self) -> str:
        return self.title



# Weekly and sessional assignments
class assignments(models.Model):
    # subject/course the assignment belongs to
    subject = models.CharField(max_length=200)
    teacher = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    # time before the assignment should/must be submitted
    due = models.DateField()
    created_at = models.DateField(default=now)

    def __str__(self) -> str:
        return self.title


class class_tests(models.Model):
    # Class test types enum
    class CtType(models.enums.Choices):
        MCQ = "mcq"
        WRITTEN = "written"
        VIVA = "viva"
    
    # subject/course the class test belongs to
    subject = models.CharField(max_length=200)
    teacher = models.CharField(max_length=100)
    about = models.TextField()
    # time when the class test will be held
    occurring = models.DateField()
    time = models.TimeField()
    # class text type field (can be either mcq or written)
    type = models.CharField(max_length=10, choices=CtType.choices, blank=True) 
    created_at = models.DateField(default=now)
    sec = models.TextField(max_length=10)
    #section
    def __str__(self) -> str:
        return self.about


class helpwewant(models.Model):
    student_id = models.CharField(max_length=7)
    question = models.TextField(max_length=500) 
    answered_by = models.TextField(max_length=15, blank=True)
    asnwer = models.TextField(max_length=500, blank=True)


    def __str__(self) -> str:
        return self.question


######## ROUTINE ######################################################################

class routineTasks(models.Model):

    class DayType(models.enums.Choices):
        SAT = "saturday"
        SUN = "sunday"
        MON = "monday"
        TUE = "tuesday"
        WED = "wednesday"
        THUR = "thursday"
        FRI = "friday"

    day = models.CharField(max_length=10, choices=DayType.choices) 
    course = models.TextField(max_length=10)
    teacher = models.TextField(max_length=20)
    time = models.TimeField()
    roomNo = models.TextField(max_length=100, blank=True)
    linkToClass = models.URLField(blank=True)

    def __str__(self) -> str:
        return self.course
