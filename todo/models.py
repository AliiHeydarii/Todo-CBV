from django.db import models

# Create your models here.


class Todo(models.Model):
    class TodoStatus(models.TextChoices):
        DONE = 'Done' , 'Done'
        PENDING = 'Pending' , 'Pending'
        NOTSTARTED = 'NotStarted' , 'NotStarted'


    title = models.CharField(max_length=150)
    description = models.TextField()
    status = models.CharField(max_length=15 , choices=TodoStatus.choices)
    create_at = models.DateTimeField(auto_now_add=True)