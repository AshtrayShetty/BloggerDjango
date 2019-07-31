#To automatically create profiles for each new user

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

#User created. Sends the signal (post_save) to receiver, ie, create_profile method 
#which creates the profile for that instance
@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
	if created:
		Profile.objects.create(user=instance)

#saving the created profile
@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
	instance.profile.save()

