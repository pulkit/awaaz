from django.conf.urls.defaults import patterns,include,url

urlpatterns = patterns('',
        (r'^form/$','form.views.your_voice_form'),
        (r'^thankyou/$','form.views.your_voice_thankyou'),
        (r'^$','YourVoice.views.YourVoice'),
        (r'^(?P<article_id>\d+)/$','YourVoice.views.article_topic',),
        )
