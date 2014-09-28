from django.conf.urls import url
from mainapp import views
urlpatterns = [
    url(r'^$', "security.views.login", name='login'),
    url(r'signoff/$', "security.views.signoff", name='signoff'),
    url(r'join/$', "security.views.join", name='join'),
]
