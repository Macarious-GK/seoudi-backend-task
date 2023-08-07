from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
# Create your views here.
from datetime import datetime
from django.http import HttpResponsePermanentRedirect 
from django.urls import reverse 
from django.template import loader 
from Seoudi_Orders.models import *
from Seoudi_Orders.serializer import *
from django.views.generic.base import TemplateView 
from django.views.generic.edit import *
from rest_framework import status, viewsets, generics
from rest_framework.status import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from Tester.serializer import *
from django.core.paginator import EmptyPage, Paginator
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import permission_classes, throttle_classes
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from django.contrib.auth.models import User,Group



@api_view(['GET','POST','PUT','PATCH','DELETE'])
def customer_CR(request):
    if request.method == 'GET':
        customer = Customer.objects.all()
        serializer_customer = customerSerializer(customer,many = True)
        return Response({'Customers':serializer_customer.data},status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
          serializer_customer = customerSerializer(data = request.data)
          serializer_customer.is_valid(raise_exception=True)
          serializer_customer.save()
          return Response(serializer_customer.data, status=status.HTTP_201_CREATED)
    else:
         return Response({'message':'this method is not supported'},status=status.HTTP_405_METHOD_NOT_ALLOWED)



@api_view(['GET','PUT','PATCH','DELETE'])
def customer_UD(request, pk):
     if request.method == 'DELETE':
        try:
            item = Customer.objects.get(pk=pk)
            item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Customer.DoesNotExist:
            return Response({"error": "Item not found."}, status=status.HTTP_404_NOT_FOUND)
     else:
  
        customer = Customer.objects.get(pk = pk)
        serializer_customer = customerSerializer(customer)
        return Response(serializer_customer.data,) 




@api_view(['GET','POST','PUT','PATCH','DELETE'])
def Items(request):
    if request.method == 'GET':
        items = Order_Item.objects.all()
        serializer_items = ItemSerializer(items,many = True)
        return Response({'Items':serializer_items.data},status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
          serializer_items = ItemSerializer(data = request.data)
          serializer_items.is_valid(raise_exception=True)
          serializer_items.save()
          return Response(serializer_items.data, status=status.HTTP_201_CREATED)
    else:
         return Response({'message':'this method is not supported'},status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET','POST','PUT','PATCH','DELETE'])
def Orderdetails(request):
    if request.method == 'GET':
        order = Order_Details.objects.all()
        serializer_order = OrderSerializer(order,many = True)
        return Response({'Orders':serializer_order.data},status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
          serializer_order = OrderSerializer(data = request.data)
          serializer_order.is_valid(raise_exception=True)
          serializer_order.save()
          return Response(serializer_order.data, status=status.HTTP_201_CREATED)
    else:
         return Response({'message':'this method is not supported'},status=status.HTTP_405_METHOD_NOT_ALLOWED)