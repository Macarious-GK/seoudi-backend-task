from rest_framework import serializers
from Tester.models import *
from rest_framework.validators import UniqueTogetherValidator 
from django.contrib.auth.models import User 
import bleach

class DeskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desk_model
        fields = '__all__'


class person_Room_serializer(serializers.ModelSerializer):
    class Meta:
        model = Person_Room
        fields = '__all__'
        # depth = 1 

class RoomsSerializer(serializers.ModelSerializer):
    Desk = DeskSerializer(read_only = True)
    person = person_Room_serializer(read_only  = True)
    Desk_id = serializers.IntegerField(write_only = True)
    person_id = serializers.IntegerField(write_only = True)
    class Meta:
        model = Romes_Model_API
        fields = ['id','Name','Area','No_Beds','Desk','Desk_id','person','person_id']
        



class RatingSerializer (serializers.ModelSerializer): 
    user = serializers.PrimaryKeyRelatedField( 
    queryset=User.objects.all(), 
    default=serializers.CurrentUserDefault() )
    class Meta:
        model = Rating
        fields =  ['user', 'menuitem_id', 'rating'] 

    validators = [UniqueTogetherValidator(queryset = Rating.objects.all(),fields=['user', 'menuitem_id'])]
    extra_kwargs = {'rating': {'min_value': 0, 'max_value':5},}
