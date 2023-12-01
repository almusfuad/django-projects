from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.menu, name = 'meal'),
    path('<int:category_id>/', views.order, name = 'order'),
]