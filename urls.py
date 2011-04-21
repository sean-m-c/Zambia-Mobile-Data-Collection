from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'Project.views.home', name='home'),

    #url(r'^formlist/$', 'Project.views.home', name='home'),

    url(r'^submission/', 'mobile.views.parse', name='mobile-submission'),

    # url(r'^Project/', include('Project.foo.urls')),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': '/opt/bitnami/projects/Project/static'}),

    # Admin interface skin
    url(r'^grappelli/', include('grappelli.urls')),

    url(r'^xform_manager/', include('xform_manager.urls')),

    (r'^sentry/', include('sentry.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
