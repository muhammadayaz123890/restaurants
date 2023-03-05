from .models import *
from django.shortcuts import render ,redirect
from django.views import View


from . import models

def Home(request):
    two_restaurants = None
    three_chefs = models.Chef.objects.all()[0:4]
    data = {}
    try:
        two_restaurants = models.Restaurant.objects.all()[0:2]
        data = {
            'two_restaurants' : two_restaurants,
            'three_chefs' : three_chefs,
        }
    except:
        pass
    return render(request , 'index.html' , data)

def About(request):
    
    return render(request , 'about.html')

def Categories(request):
    names = models.Restaurant_Food_Category.objects.all()
    data = {
        'names' : names,
    }
    return render(request , 'categories.html' , data)

def Contact(request):
    return render(request , 'contact.html')

def Restaurants(request):

    if request.method == 'GET':
        food_id = request.GET.get('food_id')
    
    food_id =int(food_id)
    name_of_cat = models.Restaurant_Food_Category.objects.get(id=food_id)

    categorized_rests = models.Restaurant.objects.filter(special_food=food_id)
    
    restaurants = models.Restaurant.objects.all()
    data = {
        'rests' : restaurants,
        'cat_rests' : categorized_rests,
        'name_of_cat':name_of_cat,
    }
    return render(request , 'restaurants.html' , data)

def Restaurant(request):
    restaurant = None
    data = {}
    try:
        if request.method == 'GET':
            rest_id = request.GET.get('rest_id')

        restaurant = models.Restaurant.objects.get(id=rest_id)

        data = {
            'restaurant': restaurant,
        }
    except:
        pass
    
    return render(request , 'specific_restaurant.html' , data )

def Chef(request):

    if request.method == 'GET':
        chef_id = request.GET.get('chef_id')
    
    chef_id = int(chef_id)

    chef_instance = models.Chef.objects.get(id=chef_id)
    
    data = {
        'chef' : chef_instance
    }

    return render(request , 'chef.html' , data)

def Chefs(request):
    chefs = models.Chef.objects.all()
    data = {
        'chefs' : chefs
    }
    return render(request , 'chefs.html' , data)

def All_restaurants(request):



    all_restaurants = models.Restaurant.objects.all()
    data = {
        'all_restaurants' : all_restaurants,
    }
    return render(request , 'all_restaurants.html' , data)

def Comment(request):



    try:
        if request.method == 'POST':
            comment_value = request.POST.get('comment_value')
            name = request.POST.get('name')
            email = request.POST.get('email')
            
            new_comment = Comment(
                    comment = comment_value
                )
            new_comment.save()

            

    except:
        pass

    return redirect('homepage')