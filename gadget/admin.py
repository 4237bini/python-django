from django.contrib import admin
from gadget.models import  Smartphone, SmartphoneDetail, Smartwatch, SmartwatchDetail, Laptop, LaptopDetail


#Register your models here.
class SmartphoneAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'averageRatings', 'image']

class SmartphoneDetailAdmin(admin.ModelAdmin):
    list_display = ['user', 'status', 'review', 'ratings']   
    list_filter = ['status']

class SmartwatchAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'averageRatings', 'image']

class SmartwatchDetailAdmin(admin.ModelAdmin):
    list_display = ['user', 'status', 'review', 'ratings']   
    list_filter = ['status']

class LaptopAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'averageRatings', 'image']

class LaptopDetailAdmin(admin.ModelAdmin):
    list_display = ['user', 'status', 'review', 'ratings']   
    list_filter = ['status']        





admin.site.register(Smartphone, SmartphoneAdmin)

admin.site.register(SmartphoneDetail, SmartphoneDetailAdmin)

admin.site.register(Smartwatch, SmartwatchAdmin)

admin.site.register(SmartwatchDetail, SmartwatchDetailAdmin)

admin.site.register(Laptop, LaptopAdmin)

admin.site.register(LaptopDetail, LaptopDetailAdmin)

