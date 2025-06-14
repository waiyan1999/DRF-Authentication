from django.db import models

# Create your models here.


class ToDoList(models.Model):
    title = models.CharField()
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
