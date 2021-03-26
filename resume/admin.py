from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import PeopleMessages


admin.site.unregister(Group)
admin.site.register(PeopleMessages)


# Register your models here.
