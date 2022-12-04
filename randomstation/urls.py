from django.urls import path
from randomstation.views import *

urlpatterns = [
	path("station/", station, name="station"),
]