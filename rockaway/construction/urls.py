from django.conf.urls import patterns, url

from rockaway.construction import views


urlpatterns = patterns('',
    url('^$', views.assessment_list, name='construction.assessment_list'),
    url('^assess$', views.assess, name='construction.assess'),
    url('^detail/(?P<assessment_id>\d+)$', views.detail,
        name='construction.detail'),
)
