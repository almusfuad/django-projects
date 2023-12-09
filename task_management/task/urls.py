from django.urls import path
from . import views

urlpatterns = [
      path('add_task/', views.add_task, name='add_task'),
      path('edit_task/<int:id>', views.edit_task, name = 'edit_task'),
      path('delete_task/<int:id>', views.delete_task, name = 'delete_task'),
      path('checked/<int:id>', views.checked, name = 'checked'),
      path('completed/<int:id>', views.delete_task, name = 'completed'),
]