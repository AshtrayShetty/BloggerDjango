from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)				#Username
	image=models.ImageField(default='default.png',upload_to='profile_pics') #Profile picture. By default, it's default.png
	bio=models.TextField(blank=None)										#User bio

	def __str__(self):
		return f'{self.user.username} Profile'  							#Returns '{username} Profile' when object is called

	#Tried to resize the image (gives some errors while configuring with AWS)
	"""def save(self,*args,**kwargs):
		super().save(*args,**kwargs)

		img=Image.open(self.image.path)

		if img.height>300 or img.width>300:
			output_size=(300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)
"""
