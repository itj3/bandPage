from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'group8.views.home', name='home'),
    url(r'^homePage', 'group8.views.home', name='home'),
    url(r'^biography', 'group8.views.biography', name='biography'),
    url(r'^Discography', 'group8.views.Discography', name='Discography'),
    url(r'^Tour', 'group8.views.Tour', name='Tour'),
    url(r'^SocialMedia', 'group8.views.SocialMedia', name='SocialMedia'),
    url(r'^upcoming', 'group8.views.upcoming', name='upcoming'),

    url(r'^admin/', include(admin.site.urls)),
)
