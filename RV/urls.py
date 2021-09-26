
from django.urls import path
from .views import *

urlpatterns = [
    path('runicheskiyvosk/', RvIndex.as_view(), name="rv_index"),
    path('runicheskiyvosk_resalt/', RvResult.as_view(), name="rv_result"),

]
