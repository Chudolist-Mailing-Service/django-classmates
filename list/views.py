from django.shortcuts import render, get_object_or_404

from list.models import Group, GroupMate


def full_list_view(request):
    mates = GroupMate.objects.all()
    return render(request, 'full_list.html', {'mates': mates})


def group_list_view(request, group_name):
    mates = GroupMate.objects.filter(group__name=group_name)
    return render(request, 'group_list.html', {'mates': mates})
