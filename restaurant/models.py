from django.db import models
from django.contrib.auth.models import User
from time import time
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill,Transpose, SmartResize

#A Helper function to help with uploads.Generates a filename through a time string
def get_upload_file_name(instance,filename):
    return "uploads/restaurant_profile_pictures/%s_%s"%(str(time()).replace('.','_'),filename)

# Create your models here.

class Restaurant(models.Model):

    cityChoices = (('lusaka','Lusaka'),('kabwe','Kabwe'),('kitwe','Kitwe'),('ndola','Ndola'))
    countryChoices = (('ZM','Zambia'),)
    categoryChoices = (('PIZ','Pizza'),('SAN','Sandwiches'),('CHI','Chicken'),('GRI','Grill'))

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.FileField(upload_to=get_upload_file_name,null=True,blank=True)
    image_thumbnail250= ImageSpecField(source='image',
                                       processors=[Transpose(),SmartResize(250,250)],
                                       format='JPEG',
                                       options={'quality':80})
    
    telephone = models.CharField(max_length=200)
    addressl1 = models.CharField(max_length=200)
    addressl2 = models.CharField(max_length=200)
    city = models.CharField(max_length=10, choices=cityChoices)
    country = models.CharField(max_length=2,choices=countryChoices)

    category = models.CharField(max_length=3,choices=categoryChoices)

    date_added = models.DateField(auto_now_add=True)

    rating = models.FloatField(default=0)
    review_count = models.IntegerField(default=0)
    order_count = models.IntegerField(default=0)

    minimum_order_amount = models.FloatField(default=0)
    delivery_fee = models.FloatField(default=0)

    weekday_open = models.CharField(max_length=6,default='09:00',null=True,blank=True)
    weekday_close = models.CharField(max_length=6,default='20:00',null=True,blank=True)
    saturday_open = models.CharField(max_length=6,default='09:00',null=True,blank=True)
    saturday_close = models.CharField(max_length=6,default='20:00',null=True,blank=True)
    sunday_open = models.CharField(max_length=6,default='09:00',null=True,blank=True)
    sunday_close = models.CharField(max_length=6,default='20:00',null=True,blank=True)
    

    user = models.ForeignKey(User, related_name='restaurants')

    def __unicode__(self):
        return self.name

class MenuItem(models.Model):

    categoryChoices = (('STA','Starters'),('MAI','Main'),('DRI','Drinks'),('DES','Dessert'),('DEA','Deals'))

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200,null=True,blank=True)
    price = models.FloatField(default=0)
    price_adjusted = models.FloatField(default=0)
    category = models.CharField(max_length=3,choices=categoryChoices,blank=True,null=True)
    
    variations = models.BooleanField(default=False)
    
    restaurant = models.ForeignKey(Restaurant,related_name='menu_items')

    def __unicode__(self):
        return '%s - %s - %s'%(self.name,self.restaurant.name,self.restaurant.city)

class Order(models.Model):

    total = models.FloatField(default=0)
    date = models.DateTimeField(null=True,blank=True)
    delivery = models.FloatField(default=0)

    delivery_instructions=models.TextField(null=True,blank=True)

    longitude = models.FloatField(default=0)
    latitude = models.FloatField(default=0)

    gps = models.BooleanField(default=True)

    expiry_date = models.DateField(null=True,blank=True)
    
    completed = models.BooleanField(default=False)
    flag = models.BooleanField(default=False)
    placed = models.BooleanField(default=False)
    driver_accepted = models.BooleanField(default=False)
    driver = models.ForeignKey(User,related_name='deliveries',null=True,blank=True)
    delivered = models.BooleanField(default=False)

    user = models.ForeignKey(User,related_name='orders')
    restaurant = models.ForeignKey(Restaurant,related_name='orders')

class OrderItem(models.Model):

    name = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    price_adjusted = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)

    description = models.CharField(max_length=200,null=True,blank=True)

    order = models.ForeignKey(Order,related_name='order_items')
    item = models.ForeignKey(MenuItem,blank=True,null=True)
    

class Review(models.Model):

    rating = models.FloatField(default=0)
    description = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User,related_name='reviews')
    order = models.OneToOneField(Order,related_name='review',null=True,blank=True)
    restaurant = models.ForeignKey(Restaurant,related_name='reviews')


class MenuOption(models.Model):
    code = models.CharField(max_length=200)
    description = models.CharField(max_length=200,null=True,blank=True)
    item = models.ForeignKey(MenuItem,related_name='properties')

    def __unicode__(self):
        return '%s option - %s'%(self.code,self.item.name)

class MenuOptionValue(models.Model):
    
    description = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    price_adjusted = models.FloatField(default=0)

    option = models.ForeignKey(MenuOption,related_name='values')

    def __unicode__(self):
        return "%s - %s - %s - %s"%(self.description,self.option.code,self.option.item.name,self.option.item.restaurant.name)
    
class OrderOption(models.Model):

    code = models.CharField(max_length=10)
    description = models.CharField(max_length=200)

    order_item = models.ForeignKey(OrderItem,related_name='order_options')
    
    
class MenuExtra(models.Model):

    code = models.CharField(max_length=200)
    description = models.CharField(max_length=200,blank=True,null=True)
    price = models.FloatField(default=0)
    price_adjusted = models.FloatField(default=0)

    item = models.ForeignKey(MenuItem,related_name='extras')

    def __unicode__(self):

        return '%s - %s - %s - %s'%(self.code,self.item.name,self.item.restaurant.name,self.item.restaurant.city)

class OrderExtra(models.Model):

    code = models.CharField(max_length=200)
    description = models.CharField(max_length=200,null=True,blank=True)
    price = models.FloatField(default=0)
    price_adjusted = models.FloatField(default=0)

    order_item = models.ForeignKey(OrderItem,related_name='order_extras')

    
    

