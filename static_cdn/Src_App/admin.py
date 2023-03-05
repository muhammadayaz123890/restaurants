from django.contrib import admin

from Src_App.models import Chef, Restaurant, Restaurant_Food_Category, User


class Restaurant_admin(admin.ModelAdmin):
    list_display= ['rest_name' , 'rest_location' , 'contact_no']

class Chef_admin(admin.ModelAdmin):
    list_display= ['chef_name' ,  'chef_ranking']

class User_admin(admin.ModelAdmin):
    list_display= ['user_name' , 'user_email']
    readonly_fields= ['user_name' , 'user_email' , 'user_password' ]

class Food_Category_Admin(admin.ModelAdmin):
    list_display= ['food_name']

admin.site.register(User , User_admin)
admin.site.register(Chef , Chef_admin)
admin.site.register(Restaurant , Restaurant_admin)
admin.site.register(Restaurant_Food_Category , Food_Category_Admin)