from django.db import models
from car_details.models import CarModel

# Create your models here.
class Comment(models.Model):
      car_details = models.ForeignKey(CarModel, on_delete = models.CASCADE, related_name = 'comments')
      name = models.CharField(max_length = 30)
      email = models.EmailField()
      body = models.TextField()
      created_on = models.DateTimeField(auto_now_add = True)
      
      
      def __str__(self):
            return f'Comments by {self.name}'