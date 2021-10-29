from django.contrib import admin

# Register your models here.
from account.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['firstname','status','lastname','address','email','profileimage']
    list_filter = ['status'] 

admin.site.register(UserProfile, UserProfileAdmin)

