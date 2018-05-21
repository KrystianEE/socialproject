from django.contrib import admin
from . import models
# Register your models here.

class GroupMemberInLine(admin.TabularInline):
    model = models.GroupMembers



admin.site.register(models.Group)
