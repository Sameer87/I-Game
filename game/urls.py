from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from .views import home,Game_view,checking


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^game/$',Game_view,name='game'),
    url(r'^check/$',checking,name='check'),
]