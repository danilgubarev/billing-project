from django.contrib import admin
from .models import ShoppingComplex, Contract

# Register your models here.
admin.site.register([ ShoppingComplex, Contract])