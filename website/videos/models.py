from django.db import models
from photologue.models import Photo

class Category(models.Model):
    name = models.CharField(max_length = 200)

    def __unicode__(self):
        return u'%s'%(self.name)

class video(models.Model):
    title = models.CharField(max_length = 30)
    link = models.TextField()
    image = models.ForeignKey(Photo)
    caption = models.TextField(blank = True)
    credits = models.TextField(blank = True)
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return u'%s'%(self.title)

    def get_absolute_url(self):
        return reverse('pl-video', args=[self.title])

# Create your models here.
