from django.db.models import query
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework import permissions
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from demoapp.serializers import InterviewSerializer
from demoapp.models import Interview

from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse

# Create your views here.
class ListInterviewAPIView(ListAPIView):
    permission_classes = [TokenHasScope]
    required_scopes = ['read']
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer
    

class CreateInterviewAPIView(CreateAPIView):
    #permission_classes = [permissions.IsAuthenticated]
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer

class UpdateInterviewAPIView(UpdateAPIView):
    permission_classes = [TokenHasScope]
    required_scopes = ['write']
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer

class DeleteInterviewAPIView(DestroyAPIView):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer


class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2!')


def interview_view(request):
    return render(request, "", {})