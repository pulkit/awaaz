from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
        (r'^about/$','pages.views.about'),
        (r'^sponsors/$','pages.views.sponsors'),
        (r'^gymkhana/about/$','pages.views.about_gym'),
        (r'^gymkhana/postbearers/$','pages.views.postbearers'),
        (r'^gymkhana/calendar/$','pages.views.gym_cal'),
)
