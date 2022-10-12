from django import forms
from django.db.models.fields import DateField
from .models import *
# from django.contrib.auth import get_user_model
# User = get_user_model()
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget

class InterviewScheduleForm(forms.ModelForm):

    class Meta:
        model = Interview
        fields = ('title', 'interviewers', 'candidates', 'resume')

    def __init__(self, *args, **kwargs):
        super(InterviewScheduleForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['resume'].label = 'Resume (Optional)'
            # self.fields['patient'].queryset = User.objects.filter(user_type="P")
            # self.fields['doctor'].queryset = User.objects.filter(user_type="D")
            # self.fields["date"].label = "Date (YYYY-MM-DD)"
            # self.fields["time"].label = "Time 24 hr (HH:MM)"

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class SlotForm(forms.ModelForm):

    class Meta:
        model = Slot
        fields = ('date', 'start_time', 'end_time')
        widgets = {
            'date': DateInput(),
            'start_time': TimeInput(),
            'end_time': TimeInput(),
        }

    # def __init__(self, *args, **kwargs):
    #     super(SlotForm, self).__init__(*args, **kwargs)
        # if self.instance:
        #     self.fields['date'].widget = AdminDateWidget()
    