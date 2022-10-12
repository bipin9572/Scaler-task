from django.contrib import admin
from .models import * 
# Register your models here.

admin.site.register(Interviewer)
admin.site.register(Candidate)
admin.site.register(Interview)
admin.site.register(Slot)