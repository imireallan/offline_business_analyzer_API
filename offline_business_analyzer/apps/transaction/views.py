from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser, JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Response
from rest_framework import generics
from .serializer import OrderPaymentSerializer, TransactionSerializer, OrderSerializer, BillPaymentSerializer, \
	BillSerializer
from .models import BillPayment, Bill, OrderPayment, Order, Transaction
from rest_framework.views import APIView
from rest_framework import status


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def uploadCSV(request):
	data = {}
	status_code = None
	serializer = TransactionSerializer(data=request.FILES, context={'user': request.user})
	if serializer.is_valid():
		transaction = serializer.save()
		data['success'] = 'successfully uploaded a csv file'
		data['csv_file'] = transaction.csv_file
		status_code = status.HTTP_201_CREATED
	else:
		data = serializer.errors
		status_code = status.HTTP_400_BAD_REQUEST
	return Response(data, status=status_code)


class UploadCSV(APIView):
	serializer_class = TransactionSerializer
	parser_classes = [MultiPartParser, FormParser, JSONParser]

	permission_classes = [IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(created_by=self.request.user, context=self.request)

	def post(self, request):
		try:
			csv_file = request.FILES['csv_file']
			if not csv_file.name.endswith('.csv'):
				return Response({'error': 'please upload a csv file'})
			data_set = csv_file.read().decode('UTF-8')
			io_string = io.StringIO(data_set)
			# skipping the csv headers
			next(io_string)
			for column in csv.reader(io_string, delimiter=','):
				pass
			return Response({'message': 'upload successful'})
		except Exception as e:
			return Response(str(e))
