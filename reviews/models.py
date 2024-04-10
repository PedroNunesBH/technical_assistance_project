from django.db import models
from devices.models import Devices


class ClientsReviews(models.Model):
    client_name = models.CharField(max_length=100)
    device_id = models.ForeignKey(Devices, on_delete=models.PROTECT, related_name="device_review")
    review_description = models.TextField()
