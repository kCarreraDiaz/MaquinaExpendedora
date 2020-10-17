from django.urls import path
from . import views

app_name ='expendedora'

urlpatterns=[
    		# ex: /expendedora
   			path('',views.index, name='index'),
    		
		    ]