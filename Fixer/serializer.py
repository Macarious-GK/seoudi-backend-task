from rest_framework import serializers
from Fixer.models import *
from decimal import Decimal
import bleach


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        depth = 1
# --------------------------------------------------------------------------------------------------
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class order(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'
# ----------------------------

class orderitemsSerializers(serializers.HyperlinkedModelSerializer):
    stoxk = serializers.IntegerField(source = 'inverntory')
    price_after_Tax =serializers.SerializerMethodField(method_name='cals')
    category = CategorySerializer(read_only = True)
    category_id = serializers.IntegerField(write_only = True)
    # category = serializers.HyperlinkedRelatedField(
    #     queryset = Category.objects.all(),
    #     view_name='Fixer:category-detail')
    
    class Meta:
        model = Items
        fields = ['id','title','price','stoxk','price_after_Tax','category','category_id']
        # depth =1
    def cals(self,product:Items):
        return product.price * Decimal(1.1)
    
    def validate(self, attrs):
        attrs['title'] = bleach.clean(attrs['title'])
        if(attrs['price']<2):
            raise serializers.ValidationError('Price should not be less than 2.0')
        if(attrs['inverntory']<0):
            raise serializers.ValidationError('Stock cannot be negative')
        return super().validate(attrs)