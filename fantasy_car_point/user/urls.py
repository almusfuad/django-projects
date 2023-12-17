from django.urls import path
from . import views

urlpatterns = [
      path('register/', views.UserSignup.as_view(), name = 'signup'),
      path('login/', views.UserLogin.as_view(), name = 'login'),
      path('logout/', views.UserLogout.as_view(), name = 'logout'),
      path('profile/', views.UserProfileDetails.as_view(), name = 'profile'),
      path('profile/update_profile/', views.UserProfileUpdate.as_view(), name = 'update_profile'),
      path('profile/update_password/', views.UserPasswordChange.as_view(), name = 'update_password'),
]