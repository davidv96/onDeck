from django.contrib import admin
from .models import Organization, Task

admin.site.register(Task)
admin.site.register(Organization)
