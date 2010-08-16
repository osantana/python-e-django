from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^gerenciador/', include('gerenciador.foo.urls')),

    (r'^$', 'agenda.views.lista'),
    (r'adiciona/$', 'agenda.views.adiciona'),
    (r'item/(?P<nr_item>\d+)/$', 'agenda.views.item'),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                                    {'document_root': settings.MEDIA_ROOT}),
    )

