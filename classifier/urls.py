from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'lang_identifier.views.index', name='index'),
    url(r'^analyze/', 'lang_identifier.views.analyze', name='analyze'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
]
