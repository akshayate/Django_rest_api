from django.shortcuts import render
# import viewsets
from rest_framework import viewsets

# import local data
from .serializers import ApiSerializers
from .models import apiModels

# create a viewset


class ApiViewSet(viewsets.ModelViewSet):
	# define queryset
	queryset = apiModels.objects.all()

	# specify serializer to be used
	serializer_class = ApiSerializers
