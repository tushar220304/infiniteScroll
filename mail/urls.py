from django.urls import path
from . import views
from django.conf import settings

app_name = 'mail'

urlpatterns = [
	path('', views.home, name='home'),
	path('email/<str:mail>/', views.email_subscribe, name="emailSubscribe"),
	path('infinite/', views.infiniteScroll, name="infiniteScroll"),
	path('infiniteJson/', views.infiniteScrollJSon, name="infiniteScrollJSon"),
]