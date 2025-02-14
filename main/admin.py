from django.contrib import admin
from .models import Dars, Sold_car, our_servise, Contact, Contact_S


admin.site.register(Contact_S)
admin.site.register(Dars)
admin.site.register(Sold_car)
admin.site.register(our_servise)
admin.site.register(Contact)