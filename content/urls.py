from django.conf.urls import patterns, url

from content import views

urlpatterns = patterns('',
  url(r'^list$', views.ContentList.as_view(), name='content_list'),
  url(r'^new$', views.ContentCreate.as_view(), name='content_new'),
  url(r'^edit/(?P<pk>\d+)$', views.ContentUpdate.as_view(), name='content_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.ContentDelete.as_view(), name='content_delete'),
  url(r'^main/(?P<partner>\w+)/$',views.MainView,name="main_view"),
  url(r'^feeder$',views.ContentFeeder,name="feeder")
)