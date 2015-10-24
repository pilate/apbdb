from django.conf.urls import url

import views


urlpatterns = [
    url(r'^achievements/$', views.progression.achievement_list.as_view(), name='gamedb-achievements'),
    url(r'^achievements/(?P<achievement>[\w\-_ ]+)/$', views.progression.achievement_detail.as_view(), name='gamedb-achievement-detail'),
]
