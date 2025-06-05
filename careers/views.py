from rest_framework import viewsets
from careers.models import Career
from careers.serializers import CareerModelSerializer


class CareerModelViewSet(viewsets.ModelViewSet):
    queryset = Career.objects.all()
    serializer_class = CareerModelSerializer

