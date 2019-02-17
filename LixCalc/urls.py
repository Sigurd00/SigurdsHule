from django.conf.urls import url
from django.urls import path, include
from LixCalc import views

urlpatterns = [
    url(r'^$', views.lixCalc, name='index'),
]
