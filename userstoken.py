from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

for user in User.objects.all():
	if user.groups.filter(name='tecnico_sispro').exists():
		Token.objects.get_or_create(user=user)
		print('Es tecnico sispro')
		print(user.email)