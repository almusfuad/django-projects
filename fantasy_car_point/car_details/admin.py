from django.contrib import admin
from .models import Brand, CarModel
from . import forms

# Register your models here.
class CarModelAdmin(admin.ModelAdmin):
      form = forms.CarModelForm

admin.site.register(Brand)
admin.site.register(CarModel)