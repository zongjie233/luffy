from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User
from rest_framework import serializers
import re

from .utils import get_user_by_account, get_tokens_for_user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # 增加想要加到token中的信息
        token['username'] = user.username
        # ...
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # 增加想要加到data中的信息
        data['id'] = self.user.id
        data['username'] = self.user.username
        # ...
        return data


class UserModelSerializer(serializers.ModelSerializer):
    sms_code = serializers.CharField(min_length=4, max_length=6, required=True, write_only=True, help_text="短信验证码")
    token = serializers.CharField(max_length=1024, read_only=True, help_text="token认证字符串")

    class Meta:
        model = User
        fields = ["id", "username", "mobile", "password", "sms_code", "token"]
        extra_kwargs = {
            "mobile": {
                "write_only": True,
            },
            "id": {
                "read_only": True,
            },
            "username": {
                "read_only": True,
            },
            "password": {
                "write_only": True,
            }
        }

    def validate(self, attrs):
        mobile = attrs.get('mobile')
        sms_code = attrs.get('sms_code')
        password = attrs.get('password')
        """验证手机号"""
        if not re.match(r'^1[345789]\d{9}$', mobile):
            raise serializers.ValidationError('手机号格式错误')

        # 验证手机号是否已经被注册了
        # try:
        #     user = User.objects.get(mobile=value)
        # except:
        #     user = None
        #
        # if user:
        #     raise serializers.ValidationError('当前手机号已经被注册')

        # 上面验证手机号是否存在的代码[优化版]
        ret = get_user_by_account(mobile)
        if ret is not None:
            raise serializers.ValidationError('当前手机号已经被注册')

        return attrs

    def create(self, validated_data):
        validated_data.pop('sms_code')
        raw_password = validated_data.get('password')
        hash_password = make_password(raw_password)
        # 对用户名设置默认值
        username = validated_data.get('mobile')

        user = User.objects.create(
            mobile=username,
            username=username,
            password=hash_password
        )
        user.token = get_tokens_for_user(user)
        return user
