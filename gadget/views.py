from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from gadget.forms import SmartphoneDetailForm, SmartwatchDetailForm, LaptopDetailForm
from gadget.models import SmartphoneDetail, Smartphone, Smartwatch, SmartwatchDetail, LaptopDetail, Laptop
from django.http.request import HttpRequest
#from sklearn.metrics.pairwise import cosine_similarity
from django.db.models import Case, When
from django.db.models import Avg, Count
from django.shortcuts import render,get_object_or_404,redirect
from django.http import Http404
from django.db.models import Case, When
from gadget import recommender
from gadget import popularity
from . import recommender
from . import popularity
from gadget import watchrecommender
from gadget import watchpopularity
from . import watchrecommender
from . import watchpopularity
from gadget import laptoprecommender
from gadget import laptoppopularity
from . import laptoprecommender
from . import laptoppopularity




# Create your views here.

def laptop(request):
   laptop = Laptop.objects.all()
   context={'laptop':laptop}
   return render(request, "laptopcart.html", context)

def laptopdetail(request: HttpRequest, id):
   laptop = Laptop.objects.get(id = id)
   laptopdetail = LaptopDetail.objects.filter(laptop_id = id, status=True)
   context={'laptop':laptop,
            'laptopdetail':laptopdetail}
   return render(request, "laptopdetail.html", context)    


def addlaptoprating(request: HttpRequest, id):
   url = request.META.get('HTTP_REFERER')  # get last url
     #return HttpResponse(url)
   if request.method == 'POST':  # check post
      
      form = LaptopDetailForm(request.POST)
      if form.is_valid():
        data = LaptopDetail()  # create relation with model
        
        
        data.review = form.cleaned_data['review']
        data.ratings = form.cleaned_data['ratings']
      
        data.laptop_id = id
        current_user = request.user
        data.user_id = current_user.id
        data.save()  # save data to table
        messages.info(request, "Your ratings and reviews has been sent. Thank you for your interest.")
      return HttpResponseRedirect(url)
   else:   
      return HttpResponseRedirect(url)

def laptoprecommendation(request):


   if request.user.is_authenticated:
      current_user_id= request.user.id
      predicted_items=laptoprecommender.User_item_score2(current_user_id)
      preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(predicted_items)])
      mob2 = Laptop.objects.filter(pk__in=predicted_items).order_by(preserved)

   elif not request.user.is_authenticated:
      pk_list = laptoppopularity.popularity_recommendation()
      preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(pk_list)])
      mob2 = Laptop.objects.filter(pk__in=pk_list).order_by(preserved)

   return render(request,'laptops.html',{'mob2':mob2})      

      


     

def smartwatch(request):
   smartwatch = Smartwatch.objects.all()
   context={'smartwatch':smartwatch}
   return render(request, "watchcart.html", context)

def smartwatchdetail(request, id):

   smartwatch = Smartwatch.objects.get(id = id)
   smartwatchdetail = SmartwatchDetail.objects.filter(smartwatch_id = id, status=True)
   context={'smartwatch':smartwatch,
            'smartwatchdetail':smartwatchdetail}
   return render(request, "watchdetail.html", context) 



def addsmartwatchrating(request, id):
   url = request.META.get('HTTP_REFERER')  # get last url
     #return HttpResponse(url)
   if request.method == 'POST':  # check post
      
      form = SmartwatchDetailForm(request.POST)
      if form.is_valid():
        data = SmartwatchDetail()  # create relation with model
        
        
        data.review = form.cleaned_data['review']
        data.ratings = form.cleaned_data['ratings']
      
        data.smartwatch_id = id
        current_user = request.user
        data.user_id = current_user.id
        data.save()  # save data to table
        messages.info(request, "Your ratings and reviews has been sent. Thank you for your interest.")
      return HttpResponseRedirect(url)
   else:   
      return HttpResponseRedirect(url)     


def watchrecommendation(request):


   if request.user.is_authenticated:
      current_user_id= request.user.id
      predicted_items=watchrecommender.User_item_score2(current_user_id)
      preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(predicted_items)])
      mob1 = Smartwatch.objects.filter(pk__in=predicted_items).order_by(preserved)

   elif not request.user.is_authenticated:
      pk_list = watchpopularity.popularity_recommendation()
      preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(pk_list)])
      mob1 = Smartwatch.objects.filter(pk__in=pk_list).order_by(preserved)

   return render(request,'smartwatch.html',{'mob1':mob1})


         

      
  
def smartphone(request):
   smartphone = Smartphone.objects.all()
   context={'smartphone':smartphone}
   return render(request, "phonecart.html", context)


def recommendation(request):


   if request.user.is_authenticated:
      current_user_id= request.user.id
      predicted_items=recommender.User_item_score2(current_user_id)
      preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(predicted_items)])
      mob = Smartphone.objects.filter(pk__in=predicted_items).order_by(preserved)

   elif not request.user.is_authenticated:
      pk_list = popularity.popularity_recommendation()
      preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(pk_list)])
      mob = Smartphone.objects.filter(pk__in=pk_list).order_by(preserved)

   return render(request,'smartphones.html',{'mob':mob})

   

  
def smartphonedetail(request, id):
   
   smartphone = Smartphone.objects.get(pk = id)
   smartphonedetail = SmartphoneDetail.objects.filter(smartphone_id = id, status=True)
   context={'smartphone':smartphone,
            'smartphonedetail':smartphonedetail}

   return render(request, "phonedetail.html", context) 



def addsmartphonerating(request, id):
   url = request.META.get('HTTP_REFERER')  # get last url
     #return HttpResponse(url)
   if request.method == 'POST':  # check post
      
      form = SmartphoneDetailForm(request.POST)
      if form.is_valid():
        data = SmartphoneDetail()  # create relation with model
        
        
        data.review = form.cleaned_data['review']
        data.ratings = form.cleaned_data['ratings']
      
        data.smartphone_id = id
        current_user = request.user
        data.user_id = current_user.id
        data.save()  # save data to table
        messages.info(request, "Your ratings and reviews has been sent. Thank you for your interest.")
      return HttpResponseRedirect(url)
   else:   
      return HttpResponseRedirect(url)
