from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
import datetime


class User(AbstractUser):
	is_customer = models.BooleanField(default=False)
	is_artist = models.BooleanField(default=False)

class Artist(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	name = models.CharField(max_length=50,blank=False)
	email = models.EmailField(max_length=254,blank=False)
	phone = models.CharField(max_length=15)
	address	= models.TextField()
	date = models.DateField(default=datetime.date.today)

	def __str__(self):
		return self.name

class Customer(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	name = models.CharField(max_length=50,blank=False)
	email = models.EmailField(max_length=254,blank=False)
	phone = models.CharField(max_length=15,blank=False)
	address = models.TextField()
	date = models.DateField(default=datetime.date.today)

	def __str__(self):
		return self.name

class Art(models.Model):
	Artist_id = models.ForeignKey(Artist,on_delete=models.CASCADE)
	Art_id = models.AutoField(primary_key=True)
	quantity = models.IntegerField(blank=False)
	name = models.CharField(max_length=50,blank=False)
	descrip = models.TextField(blank=False)
	price = models.CharField(max_length=12,blank=False)
	image = models.ImageField(null=False, blank=False)

	CATEGORY_GAMES		=	"Games"
	CATEGORY_FICTION	=	"Fiction"
	CATEGORY_NATURE		=	"Natures"
	CATEGORY_GEOMETRIC	=	"Geometric"
	CATEGORY_MYSTERIOUS	=	"Mysterious"
	CATEGORY_ACTORS		=	"Actors"
	CATEGORY_MULTIVERSE	=	"Multiverse"
	CATEGORY_COMICS		= 	"Comics"
	CATEGORY_REALISTIC	=	"Realistic"
	CATEGORY_CONCEPTUAL	=	"Conceptual"
	CATEGORY_ANCIENT	=	"Ancient"
	CATEGORY_OTHER		=	"Others"

	CATEGORY_STATE_CHOICES = (
		(CATEGORY_GAMES,CATEGORY_GAMES),
		(CATEGORY_FICTION, CATEGORY_FICTION),
		(CATEGORY_NATURE, CATEGORY_NATURE),
		(CATEGORY_GEOMETRIC, CATEGORY_GEOMETRIC),
		(CATEGORY_ACTORS, CATEGORY_ACTORS),
		(CATEGORY_MYSTERIOUS, CATEGORY_MYSTERIOUS),
		(CATEGORY_MULTIVERSE, CATEGORY_MULTIVERSE),
		(CATEGORY_COMICS, CATEGORY_COMICS),
		(CATEGORY_REALISTIC, CATEGORY_REALISTIC),
		(CATEGORY_CONCEPTUAL, CATEGORY_CONCEPTUAL),
		(CATEGORY_ANCIENT, CATEGORY_ANCIENT),
		(CATEGORY_OTHER, CATEGORY_OTHER),
	)

	category = models.CharField(max_length=20,choices=CATEGORY_STATE_CHOICES,default=CATEGORY_OTHER)

	def __str__(self):
		return self.name

class Order(models.Model):
	O_id = models.AutoField(primary_key=True)
	Art_id = models.ForeignKey(Art,on_delete=models.CASCADE)
	orderedBy = models.ForeignKey(Customer,on_delete=models.CASCADE)
	total_amount = models.IntegerField(default=0)
	timestamp = models.DateTimeField(auto_now_add=True)
	delivery_addr = models.TextField()
	quantity = models.IntegerField(default=1)

	ORDER_STATE_WAITING 	 = "Waiting"
	ORDER_STATE_PLACED 		 = "Placed"
	ORDER_STATE_ACKNOWLEDGED = "Acknowledged"
	ORDER_STATE_COMPLETED    = "Completed"
	ORDER_STATE_CANCELLED    = "Cancelled"
	ORDER_STATE_DISPATCHED   = "Dispatched"

	ORDER_STATE_CHOICES = (
		(ORDER_STATE_WAITING,ORDER_STATE_WAITING),
	    (ORDER_STATE_PLACED, ORDER_STATE_PLACED),
	    (ORDER_STATE_ACKNOWLEDGED, ORDER_STATE_ACKNOWLEDGED),
	    (ORDER_STATE_COMPLETED, ORDER_STATE_COMPLETED),
	    (ORDER_STATE_CANCELLED, ORDER_STATE_CANCELLED),
	    (ORDER_STATE_DISPATCHED, ORDER_STATE_DISPATCHED)
	)

	status = models.CharField(max_length=50,choices=ORDER_STATE_CHOICES,default=ORDER_STATE_WAITING)

	def __str__(self):
		return str(self.O_id) +' '+self.status


# class OrderItem(models.Model):
# 	id = models.AutoField(primary_key=True)
# 	Art_id = models.ForeignKey(Art, on_delete=models.CASCADE)
# 	O_id = models.ForeignKey(Order,on_delete=models.CASCADE)
# 	quantity = models.IntegerField(default=1)
	
# 	def __str__(self):
# 		return str(self.id) 

class ContactUs(models.Model):
	firstname = models.CharField(max_length=50)
	lastname = models.CharField(max_length=50)
	phone = models.CharField(max_length=14)
	email = models.EmailField(max_length=254)
	text = models.TextField()	

	def __str__(self):
		return self.firstname + ' ' + self.lastname

