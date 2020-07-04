# Create your models here.
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import pytz


TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

# Create your models here.
class Timezones(models.Model):
	user  =  models.OneToOneField(User,related_name='user_detail',on_delete=models.CASCADE)
	timezone = models.CharField(
        max_length=50,
        choices=TIMEZONES,
    )

	def __str__(self):
		return self.user.username

class Activity(models.Model):
	user =  models.ForeignKey(User,on_delete=models.CASCADE)
	start_time = models.DateTimeField(blank=True)
	end_date = models.DateTimeField(blank=True)
	
	class Meta:
		default_related_name = 'activity'
	def __str__(self):
		return self.user.username

