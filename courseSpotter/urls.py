from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^course/(?P<course_id>[a-zA-Z]{4}[0-9]{3})/$', views.course_detail, name="course_detail")
]