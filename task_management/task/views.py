from django.shortcuts import render

# Create your views here.
def add_task(request):
      return render(request, 'task/add_task.html')