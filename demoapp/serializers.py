from rest_framework import serializers
from demoapp.models import Interview

class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = "__all__"
