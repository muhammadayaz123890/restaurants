from rest_framework import serializers 
from .models import *

class Restaurant_serializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = "__all__"
    
class Chef_serializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Chef
        fields = "__all__"

class Restaurant_Food_Category_serializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Restaurant_Food_Category
        fields = "__all__"
    