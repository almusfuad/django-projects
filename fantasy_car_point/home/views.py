from django.shortcuts import render
from django.views.generic import TemplateView
from car_details.models import Brand, CarModel

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['models'] = CarModel.objects.all()
        print(context)
        return context