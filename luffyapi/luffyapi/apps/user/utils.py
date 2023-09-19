from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from .models import User


def get_user_by_account(account):
    try:
        user = User.objects.get(Q(username=account) | Q(email=account) | Q(mobile=account))
    except User.DoesNotExist:
        return None
    return user

class MyCustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None
