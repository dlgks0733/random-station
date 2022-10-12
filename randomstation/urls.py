from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from randomstation.views import *

router = DefaultRouter()
router.register(r'station', StationModelViewSet)

urlpatterns = [
	path("status_check/", status_check, name="status_check"),
	path('', include(router.urls))
]