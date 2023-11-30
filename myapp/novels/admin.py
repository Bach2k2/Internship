from django.contrib import admin

# Register your models here.
from .models import Novel,Category

admin.site.register(Novel)
admin.site.register(Category)