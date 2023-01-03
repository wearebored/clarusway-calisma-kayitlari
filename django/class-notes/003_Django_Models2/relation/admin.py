from django.contrib import admin
from .models import (
    Profile,
    Address,
    Product
)

admin.site.register(Profile)
admin.site.register(Address)
admin.site.register(Product)
