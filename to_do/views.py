from django.shortcuts import render,get_object_or_404
from .models import ToDoListModel
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,permissions
from datetime import datetime
from .serializer import ToDoSerializer
from .permissions import IsOwnerPermissions

# Create your views here.
class AllCreateToDoView(generics.ListCreateAPIView):
    """
        it gets all to do
    """
    queryset = ToDoListModel.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = (permissions.IsAuthenticated,)

class GetToDoByUserView(generics.ListAPIView):
    def get_queryset(self):
        return ToDoListModel.objects.filter(user=self.request.user)
    serializer_class = ToDoSerializer
    permission_classes = (IsOwnerPermissions,)

class DetailUpdateDeleteToDoView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDoListModel.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = (IsOwnerPermissions,)

class StatusUpdateView(APIView):
    def get(self,request,*args,**kwargs):
        task = get_object_or_404(ToDoListModel,pk=kwargs['task_id'])
        if task.status==False:
            task.status = True
            task.update_at = datetime.now()
            task.save()
            return Response({"message":"successfully update"})
        else:
            return Response({"message":"this task already done"})

class GetToDosByStatusView(APIView):
    def get(self,request,*args,**kwargs):
        status = True if kwargs['status_type'].title()=='True' else False
        all_todo_status = ToDoListModel.objects.filter(status=status)
        serializer = ToDoSerializer(all_todo_status,many=True)
        return Response(serializer.data)
