from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.db.models.signals import pre_save

class PostData(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	description = models.TextField()
	slug = models.SlugField(max_length=100,unique=True,blank=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("apps:detail",kwargs = {'slug':self.slug})

def create_slug(instance,new_slug = None):
	slug = slugify(instance.title)
	if new_slug is not None:
		slug = new_slug
	qs = PostData.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s"%(slug,qs.first().id)
		return create_slug(instance,new_slug=new_slug)
	return slug

def pre_save_post_receiver(sender,instance,*args,**kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver,PostData)


