from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from mail.models import userInfo

class Command(BaseCommand):
	help = 'It will generate the data for random user'

	def add_arguments(self, parser):
		parser.add_argument('total', type=int, help='Indicates the number of users to be created')

	def handle(self, *args, **kwargs):
		total = kwargs['total']
		try :
			for i in range(total):
				user = userInfo(Name=get_random_string(length=50, allowed_chars='tusharKumar'),
								Username=get_random_string(length=25, allowed_chars='123456789'),
								Age=get_random_string(length=2, allowed_chars='123'),
								Description=get_random_string(length=200))
				user.save()
				self.stdout.write(self.style.SUCCESS(f'User {user.Name} created with success!'))
		except:
			self.stdout.write(self.style.WARNING(f'User not created'))