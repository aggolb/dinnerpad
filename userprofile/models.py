from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):

    cityChoices = (('lusaka','Lusaka'),('kabwe','Kabwe'),('kitwe','Kitwe'),('ndola','Ndola'))
    countryChoices = (('ZM','Zambia'),)
    
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    
    phone = models.CharField(max_length=15)
    addressl1 = models.CharField(max_length=200)
    addressl2 = models.CharField(max_length=200)

    city = models.CharField(max_length=200,choices = cityChoices)
    country = models.CharField(max_length=200,choices=countryChoices,null=True,blank=True)

    driver = models.BooleanField(default=False)

    #These deal with the referral system
    referral_points = models.IntegerField(default=0)
    referred_by=models.CharField(max_length=200,null=True,blank=True)
    first_purchase = models.BooleanField(default=False)
    #
    
    user = models.OneToOneField(User, related_name='profile')

    def __unicode__(self):
        return '%s %s'%(self.firstName,self.lastName) 
