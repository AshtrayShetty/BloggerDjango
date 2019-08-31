from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#reverse return url as string. The view takes care of the redirect part
from django.urls import reverse

# Create your models here.

class Post(models.Model):
	title=models.CharField(max_length=100) 					#Title of the blog post
	content=models.TextField()            					#Content inside the blog post
	date_posted=models.DateTimeField(default=timezone.now)  #Saves the date on which the content was uploaded
	author=models.ForeignKey(User,on_delete=models.CASCADE) #Name of the author of the post

	def __str__(self):
		return self.title 									#Returns the title of the post when object is called

	def get_absolute_url(self):
		return reverse('post-detail',kwargs={'pk':self.pk}) #Gets the absolute (not hardcoded) url of the post 
															#(uses the primary key of the post for display)