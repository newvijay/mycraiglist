from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Create your views here.

def home(request):
    return render(request,'base.html')

def new_search(request):
    search=request.POST.get('search')
    print(search)
    frontend={
        'search':search
    }
    return render(request,'myapp/new_search.html',frontend)