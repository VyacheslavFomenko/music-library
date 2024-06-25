from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from listener.models import Listener


# Register your models here.


@admin.register(Listener)
class ListenerAdmin(UserAdmin):
    pass

