from urllib import response
from django.http import JsonResponse
from .serializers import BeverageSerializer
from .models import Beverages
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status


@api_view(["GET","POST"])
def drink_list(request,format=None):
    if request.method=='GET':
        drinks=Beverages.objects.all()
        serializer=BeverageSerializer(drinks , many=True)
        return Response(serializer.data)

    if request.method=='POST':
        serializer = BeverageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)

@api_view(["GET","PUT","DELETE"])
def drink_detail(request, id,format=None):
    try:
        drink=Beverages.objects.get(pk=id)
    except:
        return response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer = BeverageSerializer(drink)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer = BeverageSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method=='DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)