from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView




# Create your views here.
class UserRegistration(CreateView):
      form_class = UserCreationForm
      template_name = 'authentication.html'
      success_url = reverse_lazy('login')
      
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
            return reverse_lazy('profile')
      
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


class UserLogout(LogoutView):
      def get_success_url(self):
            messages.success(self.request, 'Logged out successfully')
            return reverse_lazy('home')
      

class UserProfileDetails(DetailView):
      model = User
      template_name = 'profile.html'
      context_object_name = 'user'
      
      def get_object(self, queryset = None):
            return self.request.user
      
class UserProfileUpdate(UpdateView):
      model = User
      form_class = forms.UserForm
      template_name = 'update.html'
      success_url = reverse_lazy('profile')
      
      
      def get_object(self, queryset = None):
            return self.request.user
      
      def form_valid(self, form):
            response = super().form_valid(form)
            messages.success(self.request, 'Update profile information successfully')
            return response
      
      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['type'] = 'Profile'
            return context
      
      
class UserPasswordChange(PasswordChangeView):
      template_name = 'update.html'
      success_url = reverse_lazy('profile')
      
      
      def form_valid(self, form):
            response = super().form_valid(form)
            messages.success(self.request, 'Password changed successfully')
            return response
      
      def form_invalid(self, form):
            response = super().form_invalid(form)
            messages.error(self.request, 'Invalid password')
      
      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['type'] = 'Password'
            return context
      