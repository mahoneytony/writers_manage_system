from django.contrib import admin
from django.contrib.auth.models import User
from app1.models import Order_model, UserProfile
# Register your models here.

admin.site.register(Order_model)
admin.site.register(UserProfile)
