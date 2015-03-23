from django.conf.urls import patterns, include, url
from django.contrib import admin
import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^', views.merhaba_django),
    url(r'^admin/', include(admin.site.urls)),
)
