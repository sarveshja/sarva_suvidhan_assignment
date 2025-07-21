from django.urls import path
from .views import *

urlpatterns = [
    path('icf-wheel/', IcfWheelMeasurementSearchCreateAPIView.as_view(), name='icf-wheel-search-create'),
    path('icf-bogie/', IcfBogieChecksheetCreateAPIView.as_view(), name='icf-bogie-create'),
]
