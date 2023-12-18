from django import forms
from . import models
from datetime import datetime


class CarModelForm(forms.ModelForm):
      class Meta:
            model = models.CarModel
            fields = '__all__'
            widgets = {
                  'model_year' : forms.SelectDateWidget(years = range(1650, datetime.now().year + 1))                  
            }