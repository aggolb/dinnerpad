from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Referral(models.Model):

    user1 = models.ForeignKey(User,related_name='referrals')
    user2 = models.OneToOneField(User,related_name='referred_by')
    activated = models.BooleanField(default=False)
    
    
