from django.db.models import query
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from demoapp.serializers import InterviewSerializer
from demoapp.models import Interview

# Create your views here.
class ListInterviewAPIView(ListAPIView):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer

class CreateInterviewAPIView(CreateAPIView):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer

class UpdateInterviewAPIView(UpdateAPIView):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer

class DeleteInterviewAPIView(DestroyAPIView):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer
