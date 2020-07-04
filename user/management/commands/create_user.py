from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
import random 
from pytz import all_timezones
from user.models import Timezones,Activity
from datetime import datetime,timedelta



# min_year=1900
# max_year=datetime.now().year

# start = datetime(min_year, 1, 1, 00, 00, 00)
# years = max_year - min_year+1
# end = start + timedelta(days=365 * years)

# for i in range(10):
#     random_date = start + (end - start) * random.random()
#     print(random_date)

# #done

# or a function
def gen_datetime(min_year=1900, max_year=datetime.now().year):
    # generate a datetime in format yyyy-mm-dd hh:mm:ss.000000
    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    return start + (end - start) * random.random()

# python manage.py create_users 10

class Command(BaseCommand):
	help = 'Create random users'

	def add_arguments(self, parser):
		parser.add_argument('total', type=int, help='Indicates the number of users to be created')

	def handle(self, *args, **kwargs):
		total = kwargs['total']
		try:
			for i in range(total):
				user = User(username=get_random_string(), email='', password='test123')
				user.save()
				timezone = Timezones(user=user,timezone=random.choice(all_timezones))
				timezone.save()
				activity = Activity(user=user,start_time=gen_datetime(),end_date=gen_datetime())
				activity.save()
				print("user created",i)
		except Exception as e:
			print(str(e))



        	


