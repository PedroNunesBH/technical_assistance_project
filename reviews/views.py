from django.views.generic import CreateView
from .models import ClientsReviews
from .forms import CreateClientReviewForm


class CreateClientReviewView(CreateView):
    model = ClientsReviews
    template_name = "create_client_review.html"
    form_class = CreateClientReviewForm
