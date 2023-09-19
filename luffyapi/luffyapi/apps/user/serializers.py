from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User
from rest_framework import serializers
import re

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
    def validate_mobile(self, attrs):

        """验证手机号"""
        if not re.match(r'^1[345789]\d{9}$', value):
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
        try:
            User.objects.get(mobile=value)
            # 如果有获取到用户信息,则下面的代码不会被执行,如果没有获取到用户信息,则表示手机号没有注册过,可以直接pass
            raise serializers.ValidationError('当前手机号已经被注册')
        except:
            pass

        return value