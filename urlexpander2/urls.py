from django.conf.urls import url
from . import views

urlpatterns =[
    # index / home page
    url(r'^$', views.index, name='index'),
    url(r'^expand/$', views.expand, name='expand'),
    url(r'^(?P<url_pk>[0-9]+)/delete/$', views.delete, name='delete'),
]
