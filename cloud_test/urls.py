from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'home.views.home', name = 'home'),
	url(r'^csv_data/$', 'home.views.csv_data', name = 'csv-data'),
	url(r'^csv_data_WPS/$', 'home.views.csv_data_WPS', name = 'csv-data-WPS'),
    # Examples:
    # url(r'^$', 'cloud_test.views.home', name='home'),
    # url(r'^cloud_test/', include('cloud_test.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
