from django.conf.urls.defaults import patterns, include, url
import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
        url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
        url(r'^admin/', include(admin.site.urls)),
        (r'^comments/', include('django.contrib.comments.urls')),
        (r'^photologue/', include('photologue.urls')),
        (r'^pages/',include('pages.urls')),
        (r'^form/',include('form.urls')),
        (r'^issue/',include('issue.urls')),
        #(r'^yourvoice/',include('YourVoice.urls')),
        (r'^',include('videos.urls')),
        (r'^pressroom/',include('pressroom.urls')),
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT})
  )
