from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Banner
from .serializers import BannerModelSerializer
from luffyapi.settings import constants
from .models import Nav
from .serializers import NavModelSerializer


# Create your views here.

class BannerListAPIView(ListAPIView):
    queryset = Banner.objects.filter(is_show=True, is_deleted=False).order_by("-orders", "-id")[
               :constants.BANNER_LENGTH]
    serializer_class = BannerModelSerializer


class HeaderNavListAPIView(ListAPIView):
    """导航菜单视图"""
    queryset = Nav.objects.filter(is_show=True, is_deleted=False, position=1).order_by("-orders", "-id")[
               :constants.HEADER_NAV_LENGTH]
    serializer_class = NavModelSerializer


class FooterNavListAPIView(ListAPIView):
    """导航菜单视图"""
    queryset = Nav.objects.filter(is_show=True, is_deleted=False, position=2).order_by("-orders", "-id")[
               :constants.FOOTER_NAV_LENGTH]
    serializer_class = NavModelSerializer
