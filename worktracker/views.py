from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from worktracker.serializer import TaskSerializer, EmployeeSerializer , TaskDetailSerializer, AssignedTasksSerializer, TaskCollectionSerializer  
from .models import Task, TaskCollection, Employee, AssignedTasks

@api_view(['GET', 'POST'])
def taskList(request):
    if request.method == 'GET':
        queryset = Task.objects.all()
        serializer = TaskSerializer(queryset, many=True)
        return Response({"message": "Task list view", "result" : queryset.count() , "data": serializer.data})
    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data
        return Response({"message": "Task created successfully"}, status=status.HTTP_201_CREATED)
         
@api_view()
def taskDetail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    serializer = TaskSerializer(task)
    return Response({"message": "Task detail view", "data": serializer.data}, status=status.HTTP_200_OK)

@api_view()
def employeeList(request):
    queryset = Employee.objects.all()
    serializer = EmployeeSerializer(queryset, many=True)
    return Response({"message": "Employee list view", "data": serializer.data}, status=status.HTTP_200_OK)  

@api_view()
def employeeDetail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    serializer = EmployeeSerializer(employee)
    return Response({"message": "Employee detail view", "data": serializer.data}, status=status.HTTP_200_OK)

@api_view()
def assignedTasksList(request):
    queryset = AssignedTasks.objects.all()
    serializer = AssignedTasksSerializer(queryset, many=True)
    return Response({"message": "Assigned Tasks list view", "data": serializer.data}, status=status.HTTP_200_OK)

@api_view()
def assignedTaskDetail(request, pk):
    assigned_task = get_object_or_404(AssignedTasks, pk=pk)
    serializer = AssignedTasksSerializer(assigned_task)
    return Response({"message": "Assigned Task detail view", "data": serializer.data}, status=status.HTTP_200_OK)

@api_view()
def taskCollectionList(request):
    queryset = TaskCollection.objects.all()
    serializer = TaskCollectionSerializer(queryset, many=True)
    return Response({"message": "Task Collection list view", "data": serializer.data}, status=status.HTTP_200_OK)

@api_view()
def taskCollectionDetail(request, pk):
    collection = get_object_or_404(TaskCollection, pk=pk)
    serializer = TaskCollectionSerializer(collection)
    return Response({"message": "Task Collection detail view", "data": serializer.data}, status=status.HTTP_200_OK)