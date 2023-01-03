from django.shortcuts import render
from .serializers import DrinkSerializer
from .models import Drink
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status




@api_view(['GET', 'POST'])
def get_drinks(request, format=None):
    if request.method == 'GET':
        drinks = Drink.objects.all()
        serDrink = DrinkSerializer(drinks, many=True)
        return Response(serDrink.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, pk, format=None):
    try:
        drink = Drink.objects.get(id=pk)
    except Drink.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return Response(serializer.data, status=status.HTTP_200_OK)

        return Response()
    elif request.method == 'PUT':
        serializer = DrinkSerializer(drink, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status.HTTP_200_OK)