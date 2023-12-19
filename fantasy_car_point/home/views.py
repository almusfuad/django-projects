from django.shortcuts import render
from django.views.generic import TemplateView
from car_details.models import Brand, CarModel

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = Brand.objects.all()
        
        
        brand_name = self.kwargs.get('brand_name')
        if brand_name is not None:
            context['models'] = CarModel.objects.filter(brand__brand_name = brand_name)
        else:
            context['models'] = CarModel.objects.all()
            
            
        return context

