from django.contrib import admin
from django.contrib.auth.models import User, Group as base_group

from group_list.models import Group, GroupMate

admin.site.unregister(User)
admin.site.unregister(base_group)

admin.site.register(Group)
admin.site.register(GroupMate)
