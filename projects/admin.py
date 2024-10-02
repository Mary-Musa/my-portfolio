from django.contrib import admin

# Register your models here.
# projects/admin.py

from django.contrib import admin
from projects.models import project

class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(project, ProjectAdmin)