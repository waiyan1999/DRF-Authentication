from rest_framework import serializers
from quickstart.models import ToDoList

#========= Serailzer =================
class MySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    title =serializers.CharField()
    description = serializers.CharField()
 
 
# ========= ModelSerialzer =============   
class TodoSerailizer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = ['id', 'title' ,'description']