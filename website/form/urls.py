from django.conf.urls.defaults import patterns,include,url


urlpatterns = patterns('',
        (r'^contact/thankyou/$','form.views.thankyou'),
        (r'^gymkhana/thankyou/$','form.views.gym_thankyou'),
        (r'^contact/$','form.views.contact'),
        (r'^gymkhana/contact/$','form.views.gym_contact'),
)
