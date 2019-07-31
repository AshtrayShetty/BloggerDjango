from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    #To make use of the signals.py file for creating profile
    def ready(self):
    	import users.signals