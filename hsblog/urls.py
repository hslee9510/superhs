from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^daily/$',views.daily,name='daily'),
    url(r'^todo/$',views.todo,name='todo'),
    url(r'^wish/$',views.wish,name='wish'),
    url(r'^inspiration/$',views.inspiration,name='inspiration'),
    url(r'^reference/$',views.reference,name='reference'),
    url(r'^trophy/$',views.trophy,name='trophy'),
    url(r'^daily/(?P<pk>\d+)/$',views.daily_detail,name='daily_detail'),
]
