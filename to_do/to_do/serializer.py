from rest_framework import serializers
from .models import ToDoListModel

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoListModel
        fields = ('id','task','status','created_at','update_at','user')