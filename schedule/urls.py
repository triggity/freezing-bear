from django.conf.urls import patterns, url

from schedule import views

urlpatterns = patterns('',
    url(r'^schedule/scheduledata/$', views.tableData, name="scheduledata"),
    url(r'^$', views.index, name='index'),
)
