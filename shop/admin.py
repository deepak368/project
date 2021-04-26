from django.contrib import admin

# Register your models here.
from shop.models import Brand,Mobile
admin.site.register(Brand)
admin.site.register(Mobile)