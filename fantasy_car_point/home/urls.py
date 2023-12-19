from django.urls import path
from . import views

urlpatterns = [
      path('', views.HomePageView.as_view(), name = 'home'),
      path('<str:brand_name>/', views.HomePageView.as_view(), name = 'filter_by_brand'),
      path('details/<slug:slug>/', views.DetailPageView.as_view(), name = 'car_details'),
]