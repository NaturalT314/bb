from django.contrib import admin

# Register your models here.
from .models import Lens, Frame

admin.site.register(Lens)
admin.site.register(Frame)