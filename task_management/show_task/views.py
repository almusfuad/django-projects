from django.shortcuts import render
from task.models import TaskModel

# Create your views here.
def show_task(request):
      tasks = TaskModel.objects.all()
      return render(request, 'show_task.html', {'tasks': tasks})

