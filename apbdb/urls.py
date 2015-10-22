from django.conf.urls import include, url

from gamedb import urls as gamedb_urls


urlpatterns = [
	url(r'', include(gamedb_urls)),
]
