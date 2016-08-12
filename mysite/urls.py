from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views

urlpatterns = [
#    url('^', include('django.contrib.auth.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^login/$', views.login, name='login'),
#    url(r'^$', views.login, name='login'),
#    url('^', include('django.contrib.auth.urls')),
    url(r'^logout/$', views.logout, name='logout', kwargs={'next_page': '/expander2'}), 
    url(r'', include('urlexpander2.urls')),
#    url(r'^expander/', include('urlexpander2.urls')), 
]
