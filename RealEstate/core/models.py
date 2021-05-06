from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db import models


class ListImages(models.Model):
	image = models.ImageField()

	def __str__(self):
		return "image"
	


class Comment(models.Model):
	name =  models.CharField(max_length=30)
	image = models.ImageField(default='avatar.jpg')
	email = models.EmailField(blank=True,null=True)
	comment = models.TextField()
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

	def serialize(self):
		return {
		'name':self.name,
		'email':self.email,
		'comment':self.comment,
		'date_created':self.date_created
		}
		
class Propreties(models.Model):
	title = models.CharField(max_length=30)

	mini_des = models.CharField(max_length=160,default='')
	full_description = models.TextField(default='')

	location = models.CharField(max_length=30)
	prop_type = models.CharField(max_length=30,default='')

	living_rooms = models.CharField(max_length=30,default='')
	beds_rooms = models.CharField(max_length=30,default='')
	bath_rooms = models.CharField(max_length=30,default='')
	kitchen = models.CharField(max_length=30,default='')
	extra_feature = models.CharField(max_length=30,default='',blank=True,null=True)


	air = models.CharField(max_length=30)
	status = models.CharField(max_length=30,choices=(
		('sell','sell'),
		('rent','rent')
		))
	price = models.FloatField()
	

	featured = models.BooleanField(default=False)

	principale_image = models.ImageField(default='images.png')

	list_images = models.ManyToManyField(ListImages,blank=True)

	comment = models.ManyToManyField(Comment)

	def __str__(self):
		return self.title


class Message(models.Model):
	name =  models.CharField(max_length=30)
	email = models.EmailField(blank=True,null=True)
	phone = models.CharField(max_length=30,blank=True,null=True)
	message = models.TextField()
	date_created = models.DateTimeField(auto_now_add=True)
	propretie = models.ForeignKey(Propreties,on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Owners(models.Model):
	name = models.CharField(max_length=30)
	image = models.ImageField(default='images.png')
	description = models.TextField()
	location = models.CharField(max_length=30)
	email = models.EmailField()
	office = models.CharField(max_length=30,default='')
	phone = models.CharField(max_length=30)
	wtsp = models.CharField(max_length=30)
	facebook = models.URLField(max_length=200,blank=True,null=True)
	twitter = models.URLField(max_length=200,blank=True,null=True)
	printest = models.URLField(max_length=200,blank=True,null=True)
	propreties = models.ManyToManyField(Propreties) 
	message = models.ManyToManyField(Message)
	def __str__(self):
		return self.name



class Blogs(models.Model):
	title = models.CharField(max_length=30)
	image = models.ImageField() 
	mini_des = models.CharField(max_length=200)
	description = models.TextField()
	date_created = models.DateTimeField(auto_now_add=True)
	comment = models.ManyToManyField(Comment)

	def __str__(self):
		return self.title


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)