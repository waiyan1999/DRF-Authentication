from django.db import models

# Create your models here.


class ToDoList(models.Model):
    title = models.CharField(max_length=100,blank=True,null=True)
    description = models.TextField(max_length=200,blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
