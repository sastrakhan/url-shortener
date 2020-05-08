from django.contrib import admin
from .models import URL, URLVisit, CustomURL

# Register your models here.
admin.site.register(URL)
admin.site.register(URLVisit)
admin.site.register(CustomURL)