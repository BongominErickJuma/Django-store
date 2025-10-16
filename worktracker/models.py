from django.db import models

class TaskCollection(models.Model):
    label=models.CharField(max_length=50)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Task(models.Model):
    title=models.CharField(max_length=50)
    slug=models.SlugField(default="_")
    due_date=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    collection=models.ForeignKey(TaskCollection, on_delete=models.CASCADE, null=True, blank=True)
    description=models.TextField()

class Employee(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254, unique=True)
    phone=models.CharField(max_length=15, unique=True)
    position=models.CharField(max_length=50)

class AssignedTasks(models.Model):
    employee=models.ForeignKey(Employee, on_delete=models.CASCADE)
    task=models.ForeignKey(Task, on_delete=models.CASCADE)
    assigned_at=models.DateTimeField(auto_now_add=True)
    completed=models.BooleanField(default=False)
    completed_at=models.DateTimeField(null=True, blank=True)
    collection=models.ForeignKey(TaskCollection, on_delete=models.CASCADE, null=True, blank=True)