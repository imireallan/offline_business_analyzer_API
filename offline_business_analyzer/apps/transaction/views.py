from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Response
from .serializer import TransactionSerializer
from rest_framework import status


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def upload_csv(request):
	data = {}
	status_code = None
	serializer = TransactionSerializer(data=request.FILES, context={'user': request.user})
	if serializer.is_valid():
		serializer.save()
		data['success'] = 'successfully uploaded a csv file'
		status_code = status.HTTP_201_CREATED
	else:
		data = serializer.errors
		status_code = status.HTTP_400_BAD_REQUEST
	return Response(data, status=status_code)
