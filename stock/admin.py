from django.contrib import admin
from .models import Customer,Artist,Art,Order,ContactUs,User

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Artist)
admin.site.register(Art)
admin.site.register(Order)
# admin.site.register(OrderItem)
admin.site.register(ContactUs)