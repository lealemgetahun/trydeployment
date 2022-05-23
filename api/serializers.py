
from .models import Classify, responce
from rest_framework import serializers



class ClassifySerializer(serializers.ModelSerializer):
	class Meta:
		model = Classify
		fields ="__all__"
class responceSerializer(serializers.ModelSerializer):
	class Meta:
		model = responce
		fields = "__all__"