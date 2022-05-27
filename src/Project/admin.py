from .models import *
from django.contrib import admin
from.models import Category, Item

admin.site.register(Item)
admin.site.register(Category)


#Cart(  Kavindi)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(DeliveryAddress)


# Register your models here.

# Delivery

admin.site.register(RouteDetails)
admin.site.register(Customer_order)
admin.site.register(Shop_order)

# Employee

admin.site.register(Employee)
