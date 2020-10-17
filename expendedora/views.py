from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

#from .models import Opcion, Pregunta  #importo los modelos

def index(request):
    return render(request,'expendedora/index.html')
			