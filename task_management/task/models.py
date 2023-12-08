from django.db import models
from category.models import CategoryModel

# Create your models here.
class TaskModel(models.Model):
      taskTitle = models.CharField(max_length = 50)
      taskDescription = models.TextField()
      is_completed = models.BooleanField(default = False)
      task_assign_date = models.DateTimeField()
      categories = models.ManyToManyField(CategoryModel)
      
      
      def __str__(self):
            return f'{self.taskTitle} - {self.task_assign_date.strftime("%d/%m/%Y")}'