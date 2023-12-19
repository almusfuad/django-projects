from django.db import models
from django.contrib.auth.models import User
from car_details.models import CarModel

# Create your models here.
class Purchase(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      product = models.ForeignKey(CarModel, on_delete = models.CASCADE)
      purchase_date = models.DateTimeField(auto_now_add = True)
      quantity = models.IntegerField(default = 1)
      total_price = models.FloatField()
      
      
      def __str__(self):
            return f'{self.user.username} - {self.product.generate_product_name()} - {self.purchase_date}'