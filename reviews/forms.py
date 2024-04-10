from django.forms import ModelForm
from .models import ClientsReviews


class CreateClientReviewForm(ModelForm):

    class Meta:
        model = ClientsReviews
        fields = "__all__"
