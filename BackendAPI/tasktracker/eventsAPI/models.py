import json
from django.db import models


class Tasks(models.Model):
    EVENTS=(
        ('START', 'start'),
        ('STOP', 'stop'),
        ('REPORT', 'report'),
    )

    events = models.CharField(max_length=10, null=True, choices=EVENTS)
    message= models.CharField(max_length = 200, null=True, blank = True)
    program_time= models.TimeField(auto_now_add=False)
    actual_time= models.TimeField(auto_now=True)
    wall_color = models.CharField(max_length=30, default='#500909')
    clock_color = models.CharField(max_length=30, default='#9c7077')
    hourhand_color = models.CharField(max_length=30, default='#630ec4')



    def __str__(self):
        return self.message


class CurrentTime(models.Model):
    seconds = models.IntegerField(null=True, blank=True)
    minutes = models.IntegerField(null=True, blank=True)
    hours = models.IntegerField(null=True, blank=True)



