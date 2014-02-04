from django.conf.urls import patterns, url

from schedule import views

urlpatterns = patterns('',
    #url(r'^scheduledata/$', views.tableData, name="scheduledata"),
    url(r'^scheduledata/$', views.scheduledata.as_view()),
    url(r'^$', views.index, name='index'),
)
