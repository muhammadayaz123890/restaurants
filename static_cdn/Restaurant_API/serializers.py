from rest_framework import serializers
from ..Src_App import models



class Restaurant_serializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Restaurant
        fields = "__all__"
    

class Chef_serializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Chef
        fields = "__all__"

