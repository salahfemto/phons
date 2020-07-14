from django.contrib import admin

# Register your models here.
from .models import numbers, cate


admin.site.register(numbers)
admin.site.register(cate)
