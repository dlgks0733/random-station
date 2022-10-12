from rest_framework import viewsets
from randomstation.models import Station
from randomstation.serializers.station import StationSerializer

# ModelViewSet - Create, Retrieve, Update, Partial_update, Destroy, List
class StationModelViewSet(viewsets.ModelViewSet):
	queryset = Station.objects.all()
	serializer_class = StationSerializer