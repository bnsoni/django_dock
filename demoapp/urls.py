from django.urls import path
from demoapp import views

urlpatterns = [
    path("", views.ListInterviewAPIView.as_view(), name="interview_list"),
    path("create/", views.CreateInterviewAPIView.as_view(), name="interview_create"),
    path("update/<int:pk>/", views.UpdateInterviewAPIView.as_view(), name="update_interview"),
    path("delete/<int:pk>/", views.DeleteInterviewAPIView.as_view(), name="delete_interview")
]
