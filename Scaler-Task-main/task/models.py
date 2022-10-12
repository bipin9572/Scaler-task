from django.db import models
from datetime import datetime


class Slot(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return str(self.date) + " " + str(self.start_time) + " - " + str(self.end_time)

    def time_object(self, o):
        start_time = o.start_time
        end_time = o.end_time
        if type(o.start_time) == str:
            try:
                start_time = datetime.strptime(o.start_time, "%H:%M").time()
            except:
                start_time = datetime.strptime(o.start_time, "%H:%M:%S").time()
        if type(o.end_time) == str:
            try:
                end_time = datetime.strptime(o.end_time, "%H:%M").time()
            except:
                end_time = datetime.strptime(o.end_time, "%H:%M:%S").time()
        return start_time, end_time


    def is_overlapping(self, o):
        start_time1, end_time1 = self.time_object(self)
        start_time2, end_time2 = self.time_object(o)
        if str(self.date) == str(o.date):
            if (start_time2 <= start_time1 and end_time2 >= start_time1) \
            or (start_time2 <= end_time1 and end_time2 >= end_time1) \
            or (start_time2 >= start_time1 and end_time2 <= end_time1) \
            or (start_time2 <= start_time1 and end_time2 >= end_time1):
                return True
            else:
                return False
        else:
            return False


class Interviewer(models.Model):
    interviewer_name = models.CharField(max_length=50)
    interviewer_email = models.EmailField(blank=True, null=True)
    scheduled_slots = models.ManyToManyField(Slot, blank=True)

    def __str__(self):
            return self.interviewer_name


class Candidate(models.Model):
    candidate_name = models.CharField(max_length=50)
    candidate_email = models.EmailField(blank=True, null=True)
    scheduled_slots = models.ManyToManyField(Slot, blank=True)
    
    def __str__(self):
        return self.candidate_name


class Interview(models.Model):
    title = models.CharField(max_length=100, default='Technical Round')
    interviewers = models.ManyToManyField(Interviewer)
    candidates = models.ManyToManyField(Candidate)
    slot = models.ForeignKey(Slot, on_delete=models.SET_NULL, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    
    def __str__(self):
        return str(self.id)

    def check_no_participants(self):
        return len(self.interviewers) >= 1 and len(self.candidates) >= 1