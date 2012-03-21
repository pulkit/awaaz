from django.conf.urls.defaults import patterns,include,url

urlpatterns = patterns('',
        (r'^awaaz/panji/$','panji.views.panji_page'),
)
