from django.contrib import admin

from .models import Blog,StaticPage

admin.site.register(Blog)
admin.site.register(StaticPage)