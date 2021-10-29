from django.urls import path

from . import views 

urlpatterns=[
    
    path('smartphone', views.smartphone, name='smartphone'),
    path('recommendation', views.recommendation, name='recommendation'),
    path('smartphonedetail/<int:id>', views.smartphonedetail, name='smartphonedetail'),
    path('addsmartphonerating/<int:id>', views.addsmartphonerating, name='addsmartphonerating'),

    path('smartwatch', views.smartwatch, name='smartwatch'),
    path('watchrecommendation', views.watchrecommendation, name='watchrecommendation'),
    path('smartwatchdetail/<int:id>', views.smartwatchdetail, name='smartwatchdetail'),
    path('addsmartwatchrating/<int:id>', views.addsmartwatchrating, name='addsmartwatchrating'),

    
    path('laptop', views.laptop, name='laptop'),
    path('laptoprecommendation', views.laptoprecommendation, name='laptoprecommendation'),
    path('laptopdetail/<int:id>', views.laptopdetail, name='laptopdetail'),
    path('addlaptoprating/<int:id>', views.addlaptoprating, name='addlaptoprating'),

    
    

]