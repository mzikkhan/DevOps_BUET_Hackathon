from django.contrib import admin

# Register your models here.
from .models import OfferedCourse
from .models import Grade

admin.site.register(Grade)
admin.site.register(OfferedCourse)