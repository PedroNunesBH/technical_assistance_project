from django.urls import path
from .views import CreateClientReviewView

urlpatterns = [
    path("create_review", CreateClientReviewView.as_view(), name="create_client_review")
]
