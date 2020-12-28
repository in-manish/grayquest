from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^login', login_view, name='login_page'),
    url(r'^logout', logout_view, name='logout'),

    url(r'', home_view, name='home_page')
]
