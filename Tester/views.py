from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
# Create your views here.
from datetime import datetime
from django.http import HttpResponsePermanentRedirect 
from django.urls import reverse 
from Tester.forms import *
from django.template import loader 
from Tester.models import *
from Tester.throttles import *
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
# Create your views here.

@api_view(['POST','GET'])
def Room_ApI_view(request):
    if request.method == 'GET':
        rooms = Romes_Model_API.objects.all()
        search_Bed = request.query_params.get('bed')
        perpage = request.query_params.get('perpage',default = 2)
        page = request.query_params.get('page',default = 1)
        if search_Bed:
            rooms = rooms.filter(No_Beds = search_Bed)
        paginator = Paginator(rooms,per_page=perpage)
        try:
            rooms = paginator.page(number=page)
        except EmptyPage:
            rooms = []
        serializer_Rooms = RoomsSerializer(rooms,many = True)
        return Response(serializer_Rooms.data)
    elif request.method == 'POST':
        serializer_Rooms = RoomsSerializer(data = request.data)
        serializer_Rooms.is_valid(raise_exception=True)
        serializer_Rooms.save()
        return Response(serializer_Rooms.validated_data,status=status.HTTP_201_CREATED)

@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({'Mwssage':'some secreat message'})

@api_view()
@permission_classes([IsAuthenticated])
def Manager_view(request):
    if request.user.groups.filter(name='Manager').exists():

        return Response({'Message':'Message for the manager only'})
    else:
        return Response({'Message':'Noooooo'},403)

@api_view()
@throttle_classes([AnonRateThrottle])
def Trottling(request):
    return Response({'Message':'Succeful'})

@api_view()
@permission_classes([IsAuthenticated])
@throttle_classes([TenCallPerMinute])
def Trottleing_auth(request):
    return Response({'Message':'trottle auth message'})


@api_view(['POST','DELETE'])
@permission_classes([IsAdminUser])
def managers(request):
    username = request.data['username']
    if username:
        user = get_object_or_404(User,username=username)
        managers = Group.objects.get(name = "Manager")
        if request.method =='POST':
            managers.user_set.add(user)
        elif request.method == 'DELETE':
            managers.user_set.remove(user)
        return Response({'message':'Okayyy'})
    return Response({'message':'Error'},status.HTTP_400_BAD_REQUEST)



class RatingsView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def get_permissions(self):
        if(self.request.method=='GET'):
            return []

        return [IsAuthenticated()]



class view_room_API(viewsets.ModelViewSet):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    queryset = Romes_Model_API.objects.all()
    serializer_class = RoomsSerializer 
    ordering_fields=['Area','No_Beds']
    # filterset_fields = ['Area']

    search_fields=['Name','person__age']


class first_class_base_views(CreateView):
    model = Menu
    fields = '__all__'
    template_name = 'Person.html'
    def get_success_url(self):
        return '/books/'


class IndexView(TemplateView): 
    template_name = 'Tester.html' 

def NUM(request):
    return HttpResponse('Fuck you cunt')

def menu(request):
    menu_items = Person.objects.all()
    items_dict = {"menu": menu_items}
    return render(request, "new.html", items_dict)

def home(request):
    return render(request,'home.html',{})
def Page2(request):
    return render(request,'base.html',{})
def Page3(request):
    return render(request,'login.html',{})