from django.db import models

# Create your models here.
from django.core.urlresolvers import reverse

class Post(models.Model):
	title = models.CharField(max_length=255)
	slug = models.SlugField(unique=True, max_length=255)
	description = models.CharField(max_length=255)
	content = models.TextField()
	published = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)

	class meta:
#Class meta is sub class of class post
		order =['-created']
	
#def needs to be tabbed once in order to be part of class meta
	def __unicode__(self):
		return u'%s' % self.title
	
	def get_absolute_url(self):
		return reverse('blog.views.post', args=[self.slug])