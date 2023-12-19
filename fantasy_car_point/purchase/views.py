from django.shortcuts import render, redirect
from . import models
from car_details.models import CarModel
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def purchase_car(request, pk):
      car_model = CarModel.objects.get(pk = pk)
      
      if car_model.quantity > 0:
            models.Purchase.objects.create(
                  user = request.user,
                  product = car_model,
                  quantity = 1,
                  total_price = car_model.price
            )
            car_model.quantity -= 1
            car_model.save()
            
            messages.success(request, 'Car purchased successfully!')
      else:
            messages.error(request, 'Sorry, this car is out of stock.')
      
      return redirect('car_details', slug = car_model.slug)