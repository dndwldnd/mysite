from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest
from django.http import HttpResponse

def index(request):
    return render(request, 'mybo/index.html', None)