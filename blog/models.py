from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#reverse return url as string. The view takes care of the redirect part
from django.urls import reverse

# Create your models here.

class Post(models.Model):
	title=models.CharField(max_length=100)
	content=models.TextField()
	date_posted=models.DateTimeField(default=timezone.now) 
	#auto_now updates date and time each time update is made
	#auto_now_add updates time and date only when the model is made
	author=models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail',kwargs={'pk':self.pk})