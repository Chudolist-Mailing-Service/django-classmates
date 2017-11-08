from django.conf.urls import url

from group_list import views

urlpatterns = [
    url(r'^$', views.full_list_view, name='full_list'),
    url(r'^(?P<group_name>[-a-z-A-Z-а-я-А-Я-0-9-_+.]+)/$', views.group_list_view,
                                             name='group_list'),
]
