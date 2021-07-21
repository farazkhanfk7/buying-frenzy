import builtins
from django.contrib import admin
from .models import Menu, Restaurant, Buyer, Purchase

# Register your models here.
admin.site.register(Menu)
admin.site.register(Restaurant)
admin.site.register(Buyer)
admin.site.register(Purchase)

