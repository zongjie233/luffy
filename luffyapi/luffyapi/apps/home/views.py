from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Banner
from .serializers import BannerModelSerializer
from luffyapi.settings import constants


# Create your views here.

# This view returns a list ofbanner objects that are displayed and not deleted.
# It uses the ListAPIView from the Django REST Framework to handle the request and response.

class BannerListAPIView(ListAPIView):
    # The queryset containsbanner objects that are displayed, not deleted, and ordered by their order and id in descending order.
    queryset = Banner.objects.filter(is_show=True,is_deleted=False).order_by("-orders", "-id")[:constants.BANNER_LENGTH]
    # The serializer_class is used to convert the queryset into a JSON format for the response.
    serializer_class = BannerModelSerializer
