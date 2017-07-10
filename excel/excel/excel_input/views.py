from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.db.models import Sum
 
import datetime #datetime을 사용하기 위해 import
# Create your views here.
def index(request): 
   return render(request, 'excel_inputs/index.html')  