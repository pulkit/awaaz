from django.conf.urls.defaults import patterns,include,url
from django.conf import settings

#from videos.views import video_gallery,video_content,coming_soon

urlpatterns = patterns('',
        url(r'^video_gallery/','videos.views.video_gallery'),
        url(r'^video_content/','videos.views.video_content'),
        url(r'^comming_soon/','videos.views.coming_soon'),
        url(r'^video_category/','videos.views.video_category'),
)


