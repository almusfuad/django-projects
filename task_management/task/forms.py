from django import forms
from django.core import validators
from . import models
from datetime import datetime, timedelta



class TaskForm(forms.ModelForm):
      class Meta:
            model = models.TaskModel
            fields = '__all__'
            exclude = ['is_completed']
            
            labels = {
                  'taskTitle': 'Title',
                  'taskDescription': 'Description',
                  'task_assign_date': 'Assign Date',
            }
            
            widgets = {
                  'taskDescription': forms.Textarea(attrs ={'rows': 5}),
                  'task_assign_date': forms.DateInput(attrs = {'type': 'date', 'min': (datetime.now().date() - timedelta(days = 0)).strftime('%Y-%m-%d')}),
            }
            
            validators = {
                  'task_assign_date': [validators.MinValueValidator(datetime.now().date())],
            }