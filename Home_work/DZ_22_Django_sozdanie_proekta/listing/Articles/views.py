# from django.shortcuts import render
import datetime
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('hello  from django')

def time(request):
    current_time = datetime.datetime.today().strftime("%H:%M:%S")
    return HttpResponse(f'Time = {current_time}')