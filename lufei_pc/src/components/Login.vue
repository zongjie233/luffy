<script setup>
import {inject, ref} from 'vue';
import {useMessage} from 'naive-ui'
import {useRouter} from 'vue-router'


const axios = inject('axios');
const settings = inject('settings');
const router = useRouter()

const login_type = ref(0);
const username = ref('');
const password = ref('');
const remember = ref(false);
const message = useMessage();
const loginHandler = async () => {
  try {
    // 请求标题
    const response = await axios.post(`${settings.HOST}/user/login/`, {
      username: username.value,
      password: password.value
    });
    console.log(response.data)
    if (remember.value) {
      // 用户选择了 "记住密码"，使用 localStorage 存储刷新令牌
      localStorage.setItem('refresh_token', response.data.refresh);
      // 同时，将访问令牌存储在 sessionStorage 中，以便在当前标签页中使用
      localStorage.setItem('user_access_token', response.data.access);
      localStorage.setItem('user_id', response.data.id);
      localStorage.setItem('user_name', response.data.username);

    } else {
      // 如果之前有存储的刷新令牌，清除它
      localStorage.removeItem('refresh_token');
      localStorage.removeItem('user_id');
      localStorage.removeItem('user_name');
      // 用户没有选择 "记住密码"，只在 sessionStorage 中存储访问令牌
      sessionStorage.setItem('user_access_token', response.data.access);
    }
    // 跳转到主页
    alert('登录成功');
    router.push('/');
  } catch (error) {
    // console.log(error);
    message.error('用户名或者密码错误,请检查后重新输入')
  }
}

const get_geetest_captcha = async () => {
  try {
    // 请求标题
    const response = await axios.get(`${settings.HOST}/user/captcha/`, {
      params: {
        username: username.value,
      }
    });
    let jsondata = JSON.parse(response.data)
    console.log(jsondata)
    initGeetest({
      // 以下配置参数来自服务端 SDK
      gt: jsondata.gt,
      challenge: jsondata.challenge,
      offline: !jsondata.success,
      new_captcha: true,
      // api_server:'api.geevisit.com' //非必须参数，添加此字段用于修改极验api域名
      product: 'popup',
      width: '100%',
    }, function (captchaObj) {
      // 这里可以调用验证实例 captchaObj 的实例方法
      captchaObj.appendTo("#geetest1"); //将验证按钮插入到宿主页面中captchaBox元素内
      captchaObj.onReady(function () {
        //your code
      }).onSuccess(function () {
        // 用户验证码正确后，发送请求给后端
        loginHandler()
      }).onError(function () {
        // 密码错误，报错
      })
    })
  } catch (error) {
    console.log(error);
  }
}

</script>

<template>

  <div class="login box">
    <img src="/static/image/Loginbg.3377d0c.jpg" alt="">
    <div class="login">
      <div class="login-title">
        <img src="/static/image/Logotitle.1ba5466.png" alt="">
        <p>帮助有志向的年轻人通过努力学习获得体面的工作和生活!</p>
      </div>
      <div class="login_box">
        <div class="title">
          <span @click="login_type=0">密码登录</span>
          <span @click="login_type=1">短信登录</span>
        </div>
        <div class="inp" v-if="login_type==0">
          <input v-model="username" type="text" placeholder="用户名 / 手机号码" class="user">
          <input v-model="password" type="password" name="" class="pwd" placeholder="密码">
          <div class="geetest" id="geetest1"></div>
          <div class="rember">
            <p>
              <input type="checkbox" v-model="remember" class="no"/>
              <span>记住密码</span>
            </p>
            <p>忘记密码</p>
          </div>
          <button @click="get_geetest_captcha" class="login_btn">登录</button>
          <p class="go_login">没有账号
            <router-link to="/user/register">立即注册</router-link>
          </p>

        </div>
        <div class="inp" v-show="login_type==1">
          <input v-model="username" type="text" placeholder="手机号码" class="user">
          <input v-model="password" type="text" class="pwd" placeholder="短信验证码">
          <button id="get_code">获取验证码</button>
          <button class="login_btn">登录</button>
          <p class="go_login">没有账号
            <router-link to="/user/register">立即注册</router-link>
          </p>
        </div>
      </div>
    </div>
  </div>

</template>

<style scoped>
.box {
  width: 100%;
  height: 100%;
  position: relative;
  overflow: hidden;
}

.box img {
  width: 100%;
  min-height: 100%;
}

.box .login {
  position: absolute;
  width: 500px;
  height: 400px;
  top: 0;
  left: 0;
  margin: auto;
  right: 0;
  bottom: 0;
  top: -338px;
}

.login .login-title {
  width: 100%;
  text-align: center;
}

.login-title img {
  width: 190px;
  height: auto;
}

.login-title p {
  font-family: PingFangSC-Regular;
  font-size: 18px;
  color: #fff;
  letter-spacing: .29px;
  padding-top: 10px;
  padding-bottom: 50px;
}

.login_box {
  width: 400px;
  height: auto;
  background: #fff;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, .5);
  border-radius: 4px;
  margin: 0 auto;
  padding-bottom: 40px;
}

.login_box .title {
  font-size: 20px;
  color: #9b9b9b;
  letter-spacing: .32px;
  border-bottom: 1px solid #e6e6e6;
  display: flex;
  justify-content: space-around;
  padding: 50px 60px 0 60px;
  margin-bottom: 20px;
  cursor: pointer;
}

.login_box .title span:nth-of-type(1) {
  color: #4a4a4a;
  border-bottom: 2px solid #84cc39;
}

.inp {
  width: 350px;
  margin: 0 auto;
}

.inp input {
  border: 0;
  outline: 0;
  width: 100%;
  height: 45px;
  border-radius: 4px;
  border: 1px solid #d9d9d9;
  text-indent: 20px;
  font-size: 14px;
  background: #fff !important;
}

.inp input.user {
  margin-bottom: 16px;
}

.geetest {
  margin-top: 16px;
}

.inp .rember {
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: relative;
  margin-top: 10px;
}

.inp .rember p:first-of-type {
  font-size: 12px;
  color: #4a4a4a;
  letter-spacing: .19px;
  margin-left: 22px;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
  /*position: relative;*/
}

.inp .rember p:nth-of-type(2) {
  font-size: 14px;
  color: #9b9b9b;
  letter-spacing: .19px;
  cursor: pointer;
}

.inp .rember input {
  outline: 0;
  width: 30px;
  height: 45px;
  border-radius: 4px;
  border: 1px solid #d9d9d9;
  text-indent: 20px;
  font-size: 14px;
  background: #fff !important;
}

.inp .rember p span {
  display: inline-block;
  font-size: 12px;
  width: 100px;
  /*position: absolute;*/
  /*left: 20px;*/

}

#geetest {
  margin-top: 20px;
}

.login_btn {
  width: 100%;
  height: 45px;
  background: #84cc39;
  border-radius: 5px;
  font-size: 16px;
  color: #fff;
  letter-spacing: .26px;
  margin-top: 30px;
}

.inp .go_login {
  text-align: center;
  font-size: 14px;
  color: #9b9b9b;
  letter-spacing: .26px;
  padding-top: 20px;
}

.inp .go_login span {
  color: #84cc39;
  cursor: pointer;
}
</style>