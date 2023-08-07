from django.shortcuts import render
from django.http import JsonResponse
from django.db import IntegrityError
from Fixer.models import *
from Fixer.serializer import *
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from rest_framework import status, viewsets, generics
from rest_framework.status import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView


@api_view(['POST','GET','PUSH'])
def books(request):
        return Response('List of Books',status=status.HTTP_200_OK)

class Orders():
     @staticmethod
     @api_view()
     def listorders(request):
          return Response({'message':'List of orders'},200)

class BookView(APIView):
     def get(self, request):
          author = request.GET.get('author')
          if(author):
               return Response({"Message":'List of books of ther author:  '+author},200)
          return Response({"Message":'Single Book}'},200)
                          
     def put(self, request):
          return Response({"title":request.data.get('title')},200)


class BookVieww(viewsets.ViewSet):
     def list(self, request):
          return Response({"Message":'All Boooks'},status.HTTP_200_OK)
     def create(self, request):
          return Response({"Message":'Create a book'},status.HTTP_201_CREATED)
     def update(self, request,pk = None):
          return Response({"Message":'update a book'},status.HTTP_200_OK)
     def retrieve(self, request,pk = None):
          return Response({"Message":'display a book'},status.HTTP_200_OK)
     def partial_retrieve(self, request,pk = None):
          return Response({"Message":'partially '},status.HTTP_200_OK)
     def destroy(self, request,pk = None):
          return Response({"Message":'destroy a record'},status.HTTP_200_OK)


@csrf_exempt
def book(request):
    if request.method == 'GET':
        books = Book.objects.all().values()
        return JsonResponse({'book':list(books)})
    elif request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        book = Book(title = title,
                    author =author,
                    price = price)
        try:
            book.save()
        except IntegrityError:
            return JsonResponse({'error':'true','message':'required field missing'},status=400)

        return JsonResponse(model_to_dict(book), status=201)
    

class MenuItems(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
     queryset = Items.objects.all()
     serializer_class = orderitemsSerializers

class SingleItemView(generics.DestroyAPIView,generics.RetrieveUpdateAPIView):
     queryset = Items.objects.all()
     serializer_class = orderitemsSerializers

class categorysesr(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
     queryset = Category.objects.all()
     serializer_class = CategorySerializer

class AuthorView(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
     queryset = Author.objects.all()
     serializer_class = AuthorSerializer




@api_view(['GET','POST'])
def orderItems(request):
     if request.method == 'GET':
          items = Items.objects.select_related('category').all()
          category_name = request.query_params.get('category')
          to_price = request.query_params.get('to_price')
          search = request.query_params.get('search')
          ordering = request.query_params.get('ordering')
          if category_name:
               items = items.filter(category__title__icontains = category_name )
          if to_price:
               items = items.filter(price__lte = to_price)
          if search:
               items = items.filter(title__icontains = search)
          if ordering:
               ordereditems = ordering.split(",")
               items = items.order_by(*ordereditems)
          serializer_itms = orderitemsSerializers(items,many =True,context={'request': request})
          return Response(serializer_itms.data)
     elif request.method == 'POST':
          serializer_itms = orderitemsSerializers(data = request.data)
          serializer_itms.is_valid(raise_exception=True)
          serializer_itms.save()
          return Response(serializer_itms.data, status=status.HTTP_201_CREATED)

     

@api_view()
def SingleOrderItem(request,pk):
     items = Items.objects.get(pk = pk)
     serializer_itms = orderitemsSerializers(items,context={'request': request})
     return Response(serializer_itms.data)

@api_view()
def category_detail(request, pk):
     category = Category.objects.get(pk = pk)
     serialized_category = CategorySerializer(category)
     return Response(serialized_category.data) 
@api_view()
def author_detail(request, pk):
     author = Author.objects.get(pk = pk)
     serialized_auther = AuthorSerializer(author)
     return Response(serialized_auther.data) 