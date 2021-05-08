from django.shortcuts import render 
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import ListView , DetailView , View
from django.core.paginator import Paginator
from .filters import PropertieFilter
import json

from django.http import JsonResponse

from .models import Propreties,Owners,Comment,Blogs,Message

from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.


class Home(View):
	def get(self,*args,**kwargs):

		properties = Propreties.objects.all()
		blogs = Blogs.objects.all()
		f = PropertieFilter(self.request.GET, queryset=properties)
		context = {
		'properties':properties[0:3],
		'blogs':blogs[0:3],
		'filter':f
		}
		return render(self.request,'home.html',context)

class PropretiesClass(View):

	def get(self,*args,**kwargs):
		objec = Propreties.objects.filter(featured=True)
		properties = Propreties.objects.all()
		paginator = Paginator(properties,10)
		page_number = self.request.GET.get('page')
		page_obj = paginator.get_page(page_number)
		is_paginated = (len(page_obj)==10)
		context = {
		'object':objec[0],
		'page_obj':page_obj,
		'is_paginated':is_paginated
		}
		return render(self.request,'listing.html',context)

	def post(self,*args,**kwargs):

		properties = Propreties.objects.all()
		f = PropertieFilter(self.request.POST, queryset=properties)
		objec = Propreties.objects.filter(featured=True)
		
		filtered = f.qs
		
		paginator = Paginator(filtered,10)
		page_number = self.request.GET.get('page')
		page_obj = paginator.get_page(page_number)
		is_paginated = (len(page_obj)==10)

		context = {
			'object':objec[0],
			'page_obj':filtered,
			'is_paginated':is_paginated
			}
		return render(self.request,'listing.html',context)


def propertie(request,pk):
	try : 

		propertie = Propreties.objects.get(pk=pk)

	except Propreties.DoesNotExist : 
		return HttpResponse('Propertie does note exists')

	owner_qs = Owners.objects.filter(propreties=propertie)
	objec = Propreties.objects.filter(featured=True)
	context = {
		'prop':objec[0],
		'propertie':propertie,
		'first': propertie.list_images.all()[0],
		'images':propertie.list_images.all()[1:],
		'Comments': propertie.comment.all()

		}
	if owner_qs.exists():
		context['owner'] = owner_qs[0]
	return render(request,'details.html',context)


class BlogsView(View):
	def get(self,*args,**kwargs):
		objec = Propreties.objects.filter(featured=True)
		blogs = Blogs.objects.all()
		paginator = Paginator(blogs,10)
		page_number = self.request.GET.get('page')
		page_obj = paginator.get_page(page_number)
		is_paginated = (len(page_obj)==10)
		context = {
			'object':objec[0],
			'page_obj':page_obj,
			'is_paginated':is_paginated
			}
		return render(self.request,'blogs.html',context)

def blog(request,pk):
	try :
		blog = Blogs.objects.get(pk=pk)
	except Blogs.DoesNotExist:
		return HttpResponse('Blog does not exists')
	objec = Propreties.objects.filter(featured=True)
	context = {
		'blog':blog,
		'object':objec[0],
		'Comments': blog.comment.all()
		}
	return render(request,'blog_detail.html',context)

def contact(request):
	if request.method == 'POST' :

		name = request.POST['name']
		email = request.POST['email']
		phone = request.POST['phone']
		message = request.POST['message']
		pk = request.POST['id']

		propertie= Propreties.objects.get(pk=pk)

		message = Message(
			name=name,
			email=email,
			phone=phone,
			message=message,
			propretie=propertie
			)

		message.save()

		owner = Owners.objects.get(propreties=propertie)

		owner.message.add(message)
		owner.save()

		return redirect('/properties')
	if request.method == 'GET':
		return render(request,'contact.html')

def PropertiesStatus(request,status):
	try :
		properties = Propreties.objects.filter(status=status)

	except Propreties.DoesNotExist:
		return HttpResponse('invalid query')

	objec = Propreties.objects.filter(featured=True)
	paginator = Paginator(properties,10)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	is_paginated = (len(page_obj)==10)
	for prop in page_obj : 
		print(prop)
	context = {
	'object':objec[0],
	'page_obj':page_obj,
	'is_paginated':is_paginated
	}
	return render(request,'listing.html',context)



# API


def CommentCreat(request,pk):
	if request.method == 'POST':
		data = json.loads(request.body)

		if data['status'] == 'propertie' : 
			obj = Propreties.objects.get(pk=pk)
		elif data['status'] == 'blog' :
			obj = Blogs.objects.get(pk=pk)
		else : 
			return JsonResponse({'error':'invalid data'},status=400)


		if ('@' not in data['email']) or (data['email'] == ''):
			comment = Comment(
					name = data['name'],
					comment=data['comment']
					)
		else : 
			comment = Comment(
					name = data['name'],
					email= data['email'],
					comment=data['comment']
					)

		comment.save()
		obj.comment.add(comment)
		obj.save()
		return JsonResponse({'valid':'valid data'},status=201)
	else : 
		return JsonResponse({'error':'invalid data'},status=400)
 