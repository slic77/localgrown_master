from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^users_list$', views.users_list),
    url(r'^user_detail/(?P<pk>[0-9a-z]+)$', views.user_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
