from django.db import models

class MainNews(models.Model):
    title=models.CharField(max_length=200)
    date=models.DateTimeField('date published')
    image=models.ImageField(upload_to='public/newsPhotos')
    short_news=models.TextField()
    main_news=models.TextField()

    def __unicode__(self):
        return u'%s'%self.title

class Institute(models.Model):
    institute=models.TextField()

    def __unicode__(self):
        return u'%s'%self.institute

class Gymkhana(models.Model):
    gymkhana=models.TextField()

    def __unicode__(self):
        return u'%s'%self.gymkhana

class External(models.Model):
    external=models.TextField()

    def __unicode__(self):
        return u'%s'%self.external

class yourvoice(models.Model):
    title=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    date=models.DateTimeField('date published')
    article=models.TextField()

    def __unicode__(self):
        return u'%s'%self.title

class ScrollNews(models.Model):
    news=models.TextField()
    image=models.ImageField(upload_to='public/newsPhotos')

    def __unicode__(self):
        return u'%s'%self.name

class panji(models.Model):
    image=models.ImageField(upload_to='public/panji')
