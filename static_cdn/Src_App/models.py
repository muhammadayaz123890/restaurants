from email.policy import default
from django.db import models



class Restaurant_Food_Category(models.Model):
    food_name = models.CharField(max_length=50)
    food_img = models.ImageField(default='' , upload_to='')

    def __str__(self):
        return self.food_name



class Restaurant(models.Model):

    rest_name = models.CharField(max_length=50)
    rest_location = models.CharField(max_length=100)
    rest_short_intro = models.CharField(max_length=100 , default='Enter your description here.')
    rest_description = models.TextField()
    rest_is_in_top_twenty = models.BooleanField(default=False)
    special_food = models.ForeignKey(Restaurant_Food_Category , on_delete=models.DO_NOTHING)
    price_category = models.CharField(max_length=60 , choices=(('Low' , 'Low') , ('Medium' , 'Medium') , ('High' , 'High') ))
    contact_no = models.CharField(max_length=50)
    rest_main_img = models.ImageField(default='' , upload_to='')
    rest_pic1 = models.ImageField(default='' , upload_to='')
    rest_pic2 = models.ImageField(default='' , upload_to='')
    rest_pic3 = models.ImageField(default='' , upload_to='')

    def __str__(self):
        return self.rest_name
        


class Chef(models.Model):
    chef_name = models.CharField(max_length=50 ,)
    chef_desc = models.TextField()
    chef_ranking = models.CharField(max_length=30 , choices=(('1' , '1' ),('2', '2'),('3','3'),('4','4'),('5','5')) , default='1')
    related_restaurant = models.ForeignKey(Restaurant , on_delete=models.DO_NOTHING)
    chef_img = models.ImageField(upload_to='' , default='')

    def __str__(self):
        return self.chef_name



class User(models.Model):
    user_name = models.CharField(max_length=50)
    user_image = models.ImageField(null=True , default='' , upload_to='')
    user_password = models.CharField(max_length=500)
    user_email = models.CharField(max_length=100)

    def __str__(self):
        return self.user_name

class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

