from django.conf.urls import patterns, include, url
from django.contrib import admin
import calc.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'(\d+)\+(\d+)', calc.views.suma, name="suma"),
    url(r'(\d+)\-(\d+)', calc.views.resta, name="resta"),
    url(r'(\d+)\*(\d+)', calc.views.mult, name="mult"),
    url(r'(\d+)/(\d+)', calc.views.div, name="div"),
    url(r'.*', calc.views.notFound, name="NotFound"),
)
