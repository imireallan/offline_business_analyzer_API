from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token

from offline_business_analyzer.apps.account.serializer import RegistrationSerializer


@api_view(['POST'])
def registration_view(request):
	data = {}
	status_code = None
	serializer = RegistrationSerializer(data=request.data)
	if serializer.is_valid():
		user = serializer.save()
		token, created = Token.objects.get_or_create(user=user)
		data['success'] = 'successfully registered a new user.'
		data['email'] = user.email
		data['username'] = user.username
		data['token'] = token.key
		status_code = status.HTTP_201_CREATED
	else:
		data = serializer.errors
		status_code = status.HTTP_400_BAD_REQUEST
	return Response(data, status=status_code)
