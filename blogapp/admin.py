from django.contrib import admin
from .models import Blog
from .models import Photo


admin.site.register(Blog)
admin.site.register(Photo)