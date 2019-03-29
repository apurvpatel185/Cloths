from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^$', AccessoriesListView.as_view(), name="accessories"),
    url(r'^(?P<slug>[\w-]+)/$', detail, name="detail"),
    url(r'^new/$', create, name='access_new'),
]