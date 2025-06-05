from rest_framework import serializers
from careers.models import Career

class CareerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = '__all__'