from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.Propreties)

admin.site.register(models.Owners)

admin.site.register(models.ListImages)


admin.site.register(models.Comment)

admin.site.register(models.Blogs)

admin.site.register(models.Message)
