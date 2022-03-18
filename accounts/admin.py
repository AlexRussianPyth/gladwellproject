from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from accounts.models import Achiever

class AchieverInline(admin.StackedInline):
    model = Achiever
    can_delete = False
    verbose_name_plural = 'achievers'

class UserAdmin(BaseUserAdmin):
    inlines = (AchieverInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)