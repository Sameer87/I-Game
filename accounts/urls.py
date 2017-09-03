from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from .views import signup,home


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', signup, name='signup'),
]
