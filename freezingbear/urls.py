from django.conf.urls import patterns, include, url

from django.views.generic import TemplateView

from django.contrib import admin
from schedule import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'freezingbear.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^schedule/', include('schedule.urls')),

    #TODO: These are temporary, put these one off views into a project
    (r'^accounts/profile', TemplateView.as_view(template_name='profile/profile.html')),
    (r'^$', TemplateView.as_view(template_name='index.html')),
)

def show_urls(urllist, depth=0):
    for entry in urllist:
        print "  " * depth, entry.regex.pattern
        if hasattr(entry, 'url_patterns'):
            show_urls(entry.url_patterns, depth + 1)

show_urls(urlpatterns)
