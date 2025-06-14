from django.shortcuts import render,HttpResponse

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from quickstart.models import ToDoList

from quickstart.serializers import MySerializer,TodoSerailizer

from rest_framework.decorators import api_view

from quickstart.models import ToDoList

from rest_framework import status

from rest_framework.response import Response


from rest_framework.views import APIView


# =================== Day 30 ========================

from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import authentication_classes,permission_classes

 

@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def toDoList(request):

    
    if request.method == 'GET':
        todo = ToDoList.objects.all()
        serializer = MySerializer(todo, many= True)
        return Response(serializer.data )
    
    elif request.method == "POST":
        data = JSONParser().parse(request)
        print(data)
        serializer = TodoSerailizer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
    else:    
        return JsonResponse(serializer.errors, status = 400)

@api_view(['GET','PUT','DELETE'])
def tododetail(request,pk):
    
    try:
        todo = ToDoList.objects.get(id=pk)
        
    except ToDoList.DoesNotExist:
        return  Response(status=status.HTTP_404_NOT_FOUND)
    
    
    if request.method == 'GET':
        serial = TodoSerailizer(todo)
        return JsonResponse(serial.data)
    
    elif request.method == 'PUT':
        serial = TodoSerailizer(todo, data = request.data)
        
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        else:
        
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class ToDoAPIView(APIView):
    #=========== Authentication-Day-30-20250613 ======================
    
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request, format=None):
        todo = ToDoList.objects.all()
        ser = MySerializer(todo, many = True)
        return Response(ser.data)
    
    def post(self, request , format = None):
        # data = JSONParser().parse(request)
        # print(data)
        serializer = TodoSerailizer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
    
    
    # authentication_classes = [ TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    
    # def get(self,request, format=None):
    #     todo = ToDoList.objects.all()
    #     ser = MySerializer(todo, many = True)
    #     return Response(ser.data)
    
    # def post(self, request , format = None):
    #     # data = JSONParser().parse(request)
    #     # print(data)
    #     serializer = TodoSerailizer(data = request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data, status = 201)
        
class ToDoDetialAPIView(APIView):
    
    def get_object(self,pk):
        try:
            return ToDoList.objects.get(id= pk)
        except ToDoList.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def get(self,request, pk , format = False):
        obj = self.get_object(pk)
        sel = TodoSerailizer(obj)
        return Response(sel.data)
    
    def put(self,request, pk , format= False):
        obj = self.get_object(pk)
        sel = TodoSerailizer(obj, data = request.data)
        if sel.is_valid():
            sel.save()
            return Response(sel.data)
        else:
            return Response(sel.errors, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, pk , format= False):
        obj = self.get_object(pk)
        obj.delete()
        return Response(self.data,status=status.HTTP_200_OK)
    
    
    
def index(request):
    return render(request, 'index.html')
    

