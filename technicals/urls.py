from django.urls import path
from technicals.views import (ListTechnicalsView, CreateTechnicalsView, UpdateTechnicalsView,
                              DeleteTechnicalsView)

urlpatterns = [
    path("list_technicals/", ListTechnicalsView.as_view(), name='list_technicals'),
    path("create_technicals/", CreateTechnicalsView.as_view(), name='create_technicals'),
    path("update_technical/<int:pk>", UpdateTechnicalsView.as_view(), name='update_technical'),
    path("delete_technical/<int:pk>", DeleteTechnicalsView.as_view(), name='delete_technical')
]
