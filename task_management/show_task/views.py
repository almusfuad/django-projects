from django.shortcuts import render
from task.models import TaskModel
from django.utils import timezone


# Create your views here.
def mark_tasks_as_completed():
      overdue_tasks = TaskModel.objects.filter(task_assign_date__lt = timezone.now().date(), is_completed = False)
      completed_tasks = TaskModel.objects.filter(is_completed = True)
      
      for task in overdue_tasks:
            task.is_completed = True
            task.save()


def show_task(request):
      mark_tasks_as_completed()
      
      tasks = TaskModel.objects.order_by('task_assign_date').all()
      return render(request, 'show_task.html', {'tasks': tasks})

