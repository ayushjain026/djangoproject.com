from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.fundraising_index, name='fundraising'),
    url(r'^thank-you/$', views.fundraising_thank_you, name='fundraising-thank-you'),
]
