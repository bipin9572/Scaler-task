from django.contrib import admin
from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static
from . import views

app_name = 'task'

urlpatterns = [
    path('', views.schedule_interview, name='schedule-interview'),
    path('update/<int:pk>/', views.reschedule_interview, name='reschedule-interview'),
    path('list/', views.interview_list, name='interview-list'),
    path('scheduled/', views.interview_scheduled, name='interview-scheduled'),
    path('rescheduled/', views.interview_rescheduled, name='interview-rescheduled'),
]