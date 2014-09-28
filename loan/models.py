import datetime
from google.appengine.ext import db
from django.contrib.auth.models import User
from django.db import models

class Loan(models.Model):
	 APPLIED = 'A'
	 FUNDED  = 'F'
	 FUNDING_IN_PROCESS = 'FIP'
	 
	 LOAN_STATES = ( ( APPLIED,'Applied' ),
	 					  ( FUNDED , 'Funded' ),
	 					  ( FUNDING_IN_PROCESS , 'Funding in Process' ) ,
	 					  )
	 borrower_id = models.ForeignKey(User)
	 loan_amount = models.FloatField()
	 applydate   = models.DateField(auto_now_add=True)
	 is_approved = models.BooleanField()
	 loan_yield  = models.FloatField()
	 approcedate = models.DateField()
	 	
class InvestorLoanMa(models.Model):
	invester_id = models.ForeignKey(User)
	amount_invested = models.FloatField()
	
'''
Payments may by the loaner
'''
class Payments( models.Model):
    paydate  = models.DateField(auto_now_add=True)   
    princpay = models.FloatField()
    intpay   = models.FloatField()
	 	 