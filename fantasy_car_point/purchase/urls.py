from django.urls import path
from . import views

urlpatterns = [
      path('<int:pk>/', views.purchase_car, name = 'buy_now'),
]