from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from rest_framework import authentication, permissions
from django.contrib.auth.models import User
import json
from .models import Activity,Timezones
from collections import defaultdict

# Create your views here.

@api_view(['GET'])
def user_info(request):
	data = User.objects.all().prefetch_related('activity')
	user_info = {"ok":True}
	user_info['members'] = []
	# s['members'] = defaultdict(list)
	
	for user in data:
		new_data = defaultdict(list)
		# s['member'].append({
		# 	'id':user.id,
		# 	'real_name':user.username,
		# 	'tz':user.user_detail.timezone,
		# 	'activity_period':[]
		# })
		new_data['id'] = user.id
		new_data['real_name'] =  user.username
		new_data['tz'] = user.user_detail.timezone
		new_data['activity_period'] = defaultdict(list)
		print("id",user.id)

		for act in user.activity.all():
			activity_period = []
			start = act.start_time.strftime("%b %d %Y %I%p")
			end = act.end_date.strftime("%b %d %Y %I%p")
			activity_period.append({
					'start_time':start,
					'end_time':end
					})

		new_data['activity_period'] = activity_period

		user_info['members'].append(new_data)

	user_info = json.loads(json.dumps(user_info))

	return Response(user_info)
