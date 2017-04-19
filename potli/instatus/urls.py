from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # return the map
    url(r'status', views.status, name='status'),
]
