from django.conf.urls import patterns, include, url
from django.contrib import admin

from obamacare.views import Homepage

admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'obamacare.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Homepage.as_view(), name="home"),
    url(r'^quote/', include('quote.urls')),
)
