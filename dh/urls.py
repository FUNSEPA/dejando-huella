from django.conf.urls import url, include
from django.contrib import admin
from django.views import static
from apps.voluntariado.views import HomeView
from . import settings

urlpatterns = [
	url(r'^media/(?P<path>.*)$', static.serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('apps.dh_auth.urls')),
    url(r'^historia/', include('apps.voluntariado.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^$', HomeView.as_view(), name="home"),
]
