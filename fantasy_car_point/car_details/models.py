from django.db import models
from django.core.validators import MaxValueValidator
from datetime import datetime

# Create your models here.
class Brand(models.Model):
      brand_name = models.CharField(max_length = 20)
      
      def __str__(self):
            return self.brand_name

def car_image_upload(instance, filename):
      return f'car_details/media/uploads/{instance.brand.brand_name}_{instance.model_name}/{filename}'


class CarModel(models.Model):
      brand = models.ForeignKey(Brand, on_delete = models.CASCADE)
      model_name = models.CharField(max_length = 30)
      title = models.CharField(max_length = 100)
      model_year = models.IntegerField()
      car_details = models.TextField()
      price = models.FloatField()
      image = models.ImageField(upload_to = car_image_upload, blank = False, null = False,)
      
      
      def __str__(self):
            return f'{self.brand} {self.model_year} {self.model_name}'