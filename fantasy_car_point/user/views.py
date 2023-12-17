from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView




# Create your views here.
class UserRegistration(CreateView):
      form_class = UserCreationForm
      template_name = 'authentication.html'
      success_url = reverse_lazy('register')
      
      def form_valid(self, form):
            response = super().form_valid(form)
            messages.success(self.request, 'Registration Successful')
            return response
      
      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['type'] = 'Register'
            return context


class UserLogin(LoginView):
      template_name = 'authentication.html'
      form_class = AuthenticationForm
      
      def get_success_url(self):
            return reverse_lazy('register')
      
      def form_valid(self, form):
            response = super().form_valid(form)
            messages.success(self.request, 'Logged in successfully')
            return response
      
      def form_invalid(self, form):
            messages.error(self.request, 'Logged in failed')
            return super().form_valid(form)
      
      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['type'] = 'Login'
            return context