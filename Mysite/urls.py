from django.conf.urls import patterns, include, url
import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'anket.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^', views.merhaba_django),
    url(r'^', include('polls.urls')),
    url(r'^anket/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
)
