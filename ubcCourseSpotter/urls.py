from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'ubcCourseSpotter.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('courseSpotter.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
