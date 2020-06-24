from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.views import Response
from rest_framework.decorators import api_view, permission_classes

from .serializer import BusinessSerializer
from .models import Business


class RegisterBusiness(generics.CreateAPIView):
	queryset = Business.objects.all()
	serializer_class = BusinessSerializer

	permission_classes = [IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


class BusinessRUDView(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = [IsAuthenticated]
	lookup_field = 'name'
	serializer_class = BusinessSerializer
	queryset = Business.objects.all()


class BusinessListView(generics.ListAPIView):
	permission_classes = [IsAuthenticated]
	serializer_class = BusinessSerializer
	queryset = Business.objects.all()


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def retrieve_business_by_owner(request):
	queryset = Business.objects.prefetch_related('owner')
	business = get_object_or_404(queryset, owner=request.user)
	serializer = BusinessSerializer(business)
	return Response(serializer.data)

