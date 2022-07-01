from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def kenny(request):
 information=Information.objects.all()
 passed_informations={'info':information}
 return render(request,'first/index.html',passed_informations)