
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$',views.index),
    url(r'^party/$',views.party),
    url(r'^diary/$',views.diary),
    url(r'^login/$',views.login),
    url(r'^reg/$',views.reg),
    url(r'^case/$',views.case),
    url(r'^safety/$',views.safety),
    url(r'^collate/$',views.CollateLogin.as_view(),name="collate"),

]