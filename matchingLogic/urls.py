from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^search/', include('haystack.urls')),
    url(r'^$', views.index, name='index'),
    url(r'(?P<individual_id>[0-9]+)/$', views.person, name='person'),
]
