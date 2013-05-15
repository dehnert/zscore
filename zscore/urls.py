from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zscore.views.home', name='home'),
    # url(r'^zscore/', include('zscore.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Admin panel:
    url(r'^admin/', include(admin.site.urls)),

    # Pages
    url(r'^leaderboard$', 'zscore.sleep.views.leaderboard'),
    url(r'^mysleep$', 'zscore.sleep.views.mysleep'),
    url(r'^$', 'zscore.sleep.views.home'),
)
