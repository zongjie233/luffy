from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken

def get_user_by_account(account):
    try:
        user = User.objects.get(Q(username=account) | Q(email=account) | Q(mobile=account))
    except User.DoesNotExist:
        return None
    return user

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return str(refresh.access_token)


class MyCustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None
