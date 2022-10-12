from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# 통신 TEST - localhost:8000/api/status_check
@api_view(['GET'])
def status_check(request):
	return Response({ "status": "OK" }, status = status.HTTP_200_OK)
