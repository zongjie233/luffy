from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path(r"login/", views.MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path(r'api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path(r'captcha/', views.CaptchaAPIView.as_view(), name='captcha'),
    path(r'register/', views.UserAPIView.as_view(), name='user_register'),
]
