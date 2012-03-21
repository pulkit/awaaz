from django.conf.urls.defaults import patterns,include,url

urlpatterns = patterns('',
        (r'^$','issue.views.show_issue'),
        (r'^search/$','issue.views.issue_search'),
)
