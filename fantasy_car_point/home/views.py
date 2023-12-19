from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView
from car_details.models import Brand, CarModel
from . import forms

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = Brand.objects.all()
        
        # browse by brand
        brand_name = self.kwargs.get('brand_name')
        if brand_name is not None:
            context['models'] = CarModel.objects.filter(brand__brand_name = brand_name)
        else:
            context['models'] = CarModel.objects.all()
                  
        return context


class DetailPageView(DetailView):
    model = CarModel
    template_name = 'details.html'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    
    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data = request.POST)
        car_details = self.get_object()
        
        if comment_form.is_valid():
            new_comment = comment_form.save(commit = False)
            new_comment.car_details = car_details
            new_comment.save()
            return redirect('car_details',slug = car_details.slug)
        return self.get(request, *args, **kwargs)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car_details = self.object
        comments = car_details.comments.all()
        comment_form = forms.CommentForm()
        context['detail'] = self.object
        context['comments'] = comments
        context['comment_form'] = comment_form
        
        
        return context