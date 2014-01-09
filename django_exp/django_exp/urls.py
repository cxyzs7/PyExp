from django.conf.urls import patterns, include, url

from django.contrib import admin
from django_exp.views import hello, current_datetime, hours_ahead

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_exp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
)
