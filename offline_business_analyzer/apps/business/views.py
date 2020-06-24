from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from .serializer import BusinessSerializer
from .models import Business


class RegisterBusiness(generics.CreateAPIView):
	queryset = Business.objects.all()
	serializer_class = BusinessSerializer

	permission_classes = [IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


class BusinessRUDView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field = 'name'
	serializer_class = BusinessSerializer
	queryset = Business.objects.all()


class BusinessListView(generics.ListAPIView):
	serializer_class = BusinessSerializer
	queryset = Business.objects.all()
