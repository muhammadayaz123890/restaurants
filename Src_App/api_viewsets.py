from rest_framework import viewsets
from .api_seriazlizers import *
from .models import *



class Restaurant_viewset(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = Restaurant_serializer


class Chef_viewset(viewsets.ModelViewSet):
    queryset = Chef.objects.all()
    serializer_class = Chef_serializer

class Food_Categories_viewset(viewsets.ModelViewSet):
    queryset = Restaurant_Food_Category.objects.all()
    serializer_class = Restaurant_Food_Category_serializer

