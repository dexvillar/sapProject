from django.conf.urls import url
from .import views

app_name = 'sapApp'

urlpatterns= [
    url(r'^$', views.loggedIn, name='loggedIn'),
    url(r'^signIn/$', views.signIn, name='signIn'),
    url(r'^signingUp/$', views.signingUp, name='signingUp'),
    url(r'^exitSession/$', views.exitSession, name='exitSession'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^students/$', views.students, name='students'),
    url(r'^students2/(?P<sapID>[0-9]+)$', views.students2, name='students2'),
    url(r'^grades/$', views.grades, name='grades'),
    url(r'^grades2/$', views.grades2, name='grades2'),
    url(r'^reports/$', views.reports, name='reports'),
    url(r'^specificreport/$', views.reports, name='specificreport'),
    url(r'^sortIt/$', views.sortIt, name='sortIt'),
    url(r'^userProfile/$', views.userProfile, name='userProfile'),
    url(r'^signUp/$', views.signUp, name='signUp'),
    url(r'^newStudent/$', views.newStudent, name='newStudent'),
]



