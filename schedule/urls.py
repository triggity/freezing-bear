from django.conf.urls import patterns, url

from schedule import views

urlpatterns = patterns('',
    #url(r'^scheduledata/$', views.tableData, name="scheduledata"),
    url(r'^sched/$', views.sched),
    url(r'^updatesched/$', views.updatesched),
    #url(r'^scheduleup/$', views.scheduleup.as_view()),
    url(r'^$', views.index, name='index'),
)
