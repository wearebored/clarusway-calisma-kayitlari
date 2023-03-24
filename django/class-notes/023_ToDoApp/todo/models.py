from django.db import models
priority_choices=[
    (1,'High'),
    (2,'Medium'),
    (3,'Low'),
]
status_choices=[
    ('c','complated'),
    ('w','waiting'),
    ('p','on progress'),
]


# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    priority=models.SmallIntegerField(choices=priority_choices,default=1)
    status=models.CharField(choices=status_choices,default='w',max_length=1)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    
