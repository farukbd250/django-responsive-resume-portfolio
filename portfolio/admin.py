
from django.contrib import admin

from portfolio.models import About, Category, Email, Global, Phone, Portfolio, Review, Service, Social,Address,Skills, Work

# Register your models here.
admin.site.register(Social)
admin.site.register(Email)
admin.site.register(Phone)
admin.site.register(Address)
admin.site.register(Global)
admin.site.register(Skills)
admin.site.register(About)
admin.site.register(Work)
admin.site.register(Service)
admin.site.register(Category)
admin.site.register(Portfolio)
admin.site.register(Review)

