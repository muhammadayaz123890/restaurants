from rest_framework import routers
from django.urls import path , include
from Src_App.api_viewsets import Chef_viewset, Food_Categories_viewset, Restaurant_viewset
from Src_App.models import Restaurant_Food_Category 



router_1 = routers.DefaultRouter()
router_1.register(r'restaurants' , Restaurant_viewset)



router_2 = routers.DefaultRouter()
router_2.register(r'chefs' , Chef_viewset)



router_3 = routers.DefaultRouter()
router_3.register(r'restaurant_categories' , Food_Categories_viewset)




urlpatterns = [
    path('' , include(router_1.urls)),
    path('' , include(router_2.urls)),
    path('' , include(router_3.urls))
]