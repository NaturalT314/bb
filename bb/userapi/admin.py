from django.contrib import admin

# Register your models here.
from .models import Glasses, User

admin.site.register(Glasses)
admin.site.register(User)