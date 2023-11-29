from django.contrib import admin

# Register your models here.

#from . models import Homepage




from . models import Customer, Menu, Homepage, Restaurant, Aboutpage, Stories

admin.site.register(Customer)

admin.site.register(Menu)

admin.site.register(Homepage)

admin.site.register(Restaurant)

admin.site.register(Aboutpage)

admin.site.register(Stories)

#admin.site.register(Lunch)

#admin.site.register(Dinner)

#admin.site.register(Desserts)

#admin.site.register(Winecard)

#admin.site.register(Drinks)