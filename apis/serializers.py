from rest_framework import serializers
from .models import apiModels

class ApiSerializers (serializers.HyperlinkedModelSerializer):
    class Meta:
        models=apiModels
        fields = ('title','description')