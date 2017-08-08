from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    url(r'^notfruit/$', views.photo_card_list),
    url(r'^notfruit/(?P<pk>[0-9]+)/$', views.photo_card_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)