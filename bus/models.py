from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
class bus(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	slug = models.SlugField(unique=True)

class track(models.Model):
	lat = models.FloatField()
	lng = models.FloatField()
	uid = models.SlugField()
	 
class user_profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	dob = models.DateField(null=True,blank=True)
	photo = models.ImageField(null=True,blank=True)

def create_slug(instance,*args,**kwargs):
	if not instance.slug:
		instance.slug = "%s-%s"%(instance.title,instance.id)
pre_save.connect(create_slug,sender=bus)




