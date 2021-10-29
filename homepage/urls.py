from django.urls import include, path


from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('search',views.search,name='search'),
    path('search_auto',views.search_auto,name='search_auto'),
    
    

]