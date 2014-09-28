import datetime
from google.appengine.ext import db
from django.contrib.auth.models import User
from django.db import models

class Account(models.Model):
    user_id   = models.ForeignKey(User)
    pannumber = models.CharField(max_length=100)
    addressa  = models.CharField(max_length=800)
    addressb  = models.CharField(max_length=800)
    city      = models.CharField(max_length=100)
    state     = models.CharField(max_length=100)
    zipcode   = models.CharField(max_length=40)
    homephone = models.CharField(max_length=40)
    mobilephone = models.CharField(max_length=40)
    joindate    = models.DateField(auto_now_add=True)
    
class BankAccount(models.Model):
	user_id       = models.ForeignKey(User)
	bankname      = models.CharField(max_length=400)
	nickname  	  = models.CharField(max_length=400)
	accountnumber = models.CharField(max_length=400)
	routingnumber = models.CharField(max_length=400)
	bankaddress   = models.CharField(max_length=800)
	bankaddressb  = models.CharField(max_length=800)
	