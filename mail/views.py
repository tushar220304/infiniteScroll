from django.shortcuts import render
from .models import Email_Subscription
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import  Email_Subscription, userInfo
from django.http import JsonResponse
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import time

def home(request):
	return render(request, 'mail/index.html')

def email_subscribe(request, mail):
	email = Email_Subscription(Email=mail, Subscribed=True)
	email.save()
	try:
		send_mail('Email added to News Letter',
				  f'Hi \
				  \nYour email {email} is succesfully added in our subscribers list.',
				  'movie220304@gmail.com', [mail])
		return JsonResponse({'status':'ok'})
	except Exception:
		return JsonResponse({'status':'not-ok'})

def infiniteScroll(request):
	users = userInfo.objects.values('id', 'Username', 'Name', 'Age')[:24]
	return render(request, 'mail/infinite.html', {'users': users})

def infiniteScrollJSon(request):
	users = userInfo.objects.only('id', 'Username', 'Name', 'Age')
	paginator = Paginator(users, 8)
	page = request.GET.get('page')
	try:
		user_page = paginator.page(page)
		users_json = serializers.serialize('json', user_page)
		time.sleep(0.5)
		return HttpResponse(users_json, content_type="text/json-comment-filtered")
	except EmptyPage:
		return JsonResponse({'page': 'empty'})
	
