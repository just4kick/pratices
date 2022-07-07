from django.shortcuts import render  
import requests
from django.template import loader  

from django.http import HttpResponse  
def index(request):
    return render(request, 'stock/index.html')

def new(request):
    return render(request,'stock/test.html')
    
def search(request):
    return render(request,'stock/search.html')    

def test(request):
    if (request.GET):
        name=request.GET["myCountry"]
        lh='https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords='
        rh='&apikey=ZAJ48HSMNW5ZF854'
        fl=lh+name+rh
        url = fl
        r = requests.get(url)
        data = r.json()
        context={
            "first":data['bestMatches'][0]['1. symbol'],
            #"second":data['bestMatches'][1]['1. symbol'],
            "text":name
        }
    
        return render(request,'stock/test.html',context)
    else:
        return render(request,'stock/test.html')


