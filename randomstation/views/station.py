from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import random
from randomstation.models import Station
from randomstation.serializers import StationSerializer

# /api/station/
@api_view(['GET'])
def station(request):
	count = Station.objects.count()
	random_id = random.randint(1, count)
	random_station = Station.objects.filter(pk=random_id)
	serializer = StationSerializer(random_station, many=True)
	return Response({ "status": "OK", "random_station": serializer.data }, status = status.HTTP_200_OK)