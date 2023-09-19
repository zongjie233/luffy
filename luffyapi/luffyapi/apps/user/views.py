import hmac
from django.http import JsonResponse
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from luffyapi.libs.geetest_lib import GeetestLib
from .serializers import MyTokenObtainPairSerializer, UserModelSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .utils import get_user_by_account
from rest_framework import status
from .models import User

GEETEST_ID = "624b6a30c6d8621fc9386c85cf798f32"
GEETEST_KEY = "e2375da2d4ed9bb903ea410991b2c382"


# Create your views here.

class MyObtainTokenPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class CaptchaAPIView(APIView):
    bypass_status = False
    user_id = 0

    def get(self, request):
        # 必传参数
        #     digestmod 此版本sdk可支持md5、sha256、hmac-sha256，md5之外的算法需特殊配置的账号，联系极验客服
        # 自定义参数,可选择添加
        #     user_id 客户端用户的唯一标识，确定用户的唯一性；作用于提供进阶数据分析服务，可在register和validate接口传入，不传入也不影响验证服务的使用；若担心用户信息风险，可作预处理(如哈希处理)再提供到极验
        #     client_type 客户端类型，web：电脑上的浏览器；h5：手机上的浏览器，包括移动应用内完全内置的web_view；native：通过原生sdk植入app应用的方式；unknown：未知
        #     ip_address 客户端请求sdk服务器的ip地址
        # bypass_status = get_bypass_cache()
        gt_lib = GeetestLib(GEETEST_ID, GEETEST_KEY)
        digestmod = "md5"
        username = request.GET.get("username")
        print("username:", username)
        user = get_user_by_account(username)
        if user is None:
            return Response({"message": "用户不存在"}, status=status.HTTP_400_BAD_REQUEST)
        self.user_id = user.id
        # TODO: 将status保存到redis
        param_dict = {"digestmod": digestmod, "username": username, "client_type": "web", "ip_address": "127.0.0.1"}
        # if self.bypass_status == "success":
        #     result = gt_lib.register(digestmod, param_dict)
        # else:
        #     result = gt_lib.local_init()
        result = gt_lib.register(digestmod, param_dict)
        print(result.data)
        # 注意，不要更改返回的结构和值类型
        return Response(result.data, content_type='application/json;charset=UTF-8')

    def post(self, request):
        challenge = request.form.get(GeetestLib.GEETEST_CHALLENGE, None)
        validate = request.form.get(GeetestLib.GEETEST_VALIDATE, None)
        seccode = request.form.get(GeetestLib.GEETEST_SECCODE, None)
        # bypass_status = get_bypass_cache()
        gt_lib = GeetestLib(GEETEST_ID, GEETEST_KEY)
        # if bypass_status == "success":
        #     result = gt_lib.successValidate(challenge, validate, seccode)
        # else:
        result = gt_lib.failValidate(challenge, validate, seccode)
        # 注意，不要更改返回的结构和值类型
        if result.status == 1:
            response = {"result": "success", "version": GeetestLib.VERSION}
        else:
            response = {"result": "fail", "version": GeetestLib.VERSION, "msg": result.msg}
        return JsonResponse(response)


class UserAPIView(CreateAPIView):
    """用户管理"""
    queryset = User.objects.all()
    serializer_class = UserModelSerializer