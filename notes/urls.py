from django.conf.urls import url
from notes import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include


urlpatterns = [
    url(r'^notes/$', views.NoteList.as_view()),
    url(r'^notes/(?P<pk>[0-9]+)/$', views.NoteDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
	url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]