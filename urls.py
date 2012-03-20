from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'awaaz.views.home', name='home'),
    # url(r'^awaaz/', include('awaaz.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	(r'^$','news.views.display_news'),
	(r'^awaaz/about/$','news.views.about'),
	(r'^awaaz/gymkhana/$','news.views.gymkhana'),
	(r'^awaaz/issues/$','issue.views.show_issue'),
	(r'^awaaz/sponsors/$','news.views.sponsors'),
	(r'^awaaz/yourvoice/$','news.views.YourVoice'),
	(r'^awaaz/contact/$','form.views.contact'),
        (r'^awaaz/news/(?P<news_id>\d+)/$','news.views.news_topic',),
	(r'^awaaz/issues/search/$','issue.views.issue_search'),
	(r'^awaaz/gymkhana/about/$','news.views.about_gym'),
	(r'^awaaz/gymkhana/postbearers/$','news.views.postbearers'),
	(r'^awaaz/gymkhana/contact/$','form.views.gym_contact'),
	(r'^awaaz/gymkhana/calendar/$','news.views.gym_cal'),
	(r'^awaaz/news/all/$','news.views.all_news'),
	(r'^comments/', include('django.contrib.comments.urls')),
	(r'^awaaz/photos/$','photos.views.photo'),
	(r'^awaaz/yourvoice/form/$','form.views.your_voice_form'),
        (r'^awaaz/yourvoice/(?P<article_id>\d+)/$','news.views.article_topic',),
	(r'^awaaz/yourvoice/thankyou/$','form.views.your_voice_thankyou'),
	(r'^awaaz/contact/thankyou/$','form.views.thankyou'),
	(r'^awaaz/gymkhana/thankyou/$','form.views.gym_thankyou'),
	(r'^awaaz/panji/$','news.views.panji_page'),
)
