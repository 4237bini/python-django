from django.shortcuts import render
from homepage.forms import SearchForm
import json
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q, F
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request
from django.shortcuts import render
from gadget.models import Smartphone, SmartphoneDetail, Smartwatch, SmartwatchDetail,  Laptop, LaptopDetail
from account.models import UserProfile
from gadget.views import recommendation, watchrecommendation, laptoprecommendation


# Create your views here.
def home(request):
    return render(request,'index.html')

def search(request):
    if request.method == 'POST': # check post
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query'] # get form input data
            
        
            smartphone = Smartphone.objects.filter(name__icontains=query)  #SELECT * FROM product WHERE title LIKE '%query%'
            smartwatch = Smartwatch.objects.filter(name__icontains=query)
            laptop = Laptop.objects.filter(name__icontains=query)
            

        
            context = {'smartphone': smartphone, 'query':query, 'smartwatch': smartwatch, 'laptop': laptop }
            return render(request, 'search.html', context)

    return HttpResponseRedirect('/')

def search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        smartphone = Smartphone.objects.filter(name__icontains=q)

        results = []
        for smartphone in smartphone:
            smartphone_json = {}
            smartphone_json = smartphone.name
            results.append(smartphone_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)