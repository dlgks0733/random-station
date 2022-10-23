from rest_framework import serializers
from randomstation.models import Station

class StationSerializer(serializers.ModelSerializer):

	def create(self, validated_data):
		Station.save(validated_data)

	class Meta:
		model = Station
		fields = ['name', 'line', 'order']