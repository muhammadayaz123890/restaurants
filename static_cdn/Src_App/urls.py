from django.urls import path
from . import views


urlpatterns = [
    path('' , views.Home , name='homepage'),
    path('categories/' , views.Categories , name='categories_page'),
    path('restaurants/' , views.Restaurants , name='categorized_restaurants_page'),
    path('restaurant/' , views.Restaurant , name='specific_restaurant'),
    path('chef/' , views.Chef , name='chef_page'),
    path('about/' , views.About , name='about_page'),
    path('chefs/' , views.Chefs , name='all_chefs_page'),
    path('all_rests/' , views.All_restaurants , name='all_restaurants_page'),
    path('contact/' , views.Contact , name='contact_page'),
    path('user_comment/' , views.Comment )
]