from django.conf.urls import url

import views


urlpatterns = [
    url(r'^achievements/$', views.progression.achievement_list.as_view(), name='gamedb-achievements'),
]
