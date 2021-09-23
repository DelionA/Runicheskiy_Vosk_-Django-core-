
from django.urls import path
from .views import RasskladView, RasskladShow

urlpatterns = [
    path('', RasskladView.as_view(), name="start_start"),
    path('rv/', RasskladShow, name="show_result")
]
