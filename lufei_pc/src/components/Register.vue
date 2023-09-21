<script setup>
import {inject, ref} from 'vue';
import {useRouter} from 'vue-router'
import {useMessage} from 'naive-ui'


const message = useMessage();
const axios = inject('axios');
const settings = inject('settings');
const router = useRouter()

const sms_code = ref("")
const mobile = ref("")
const password = ref("")

const registerHandler = async () => {
  try {
    const response = await axios.post(`${settings.HOST}/user/register/`, {
      mobile: mobile.value,
      password: password.value,
      sms_code: sms_code.value
    })
    console.log(response.data)

    // 如果之前有存储的刷新令牌，清除它
    localStorage.removeItem('refresh_token');
    localStorage.removeItem('user_id');
    localStorage.removeItem('user_name');
    // 用户没有选择 "记住密码"，只在 sessionStorage 中存储访问令牌
    sessionStorage.setItem('user_access_token', response.data.token);
    alert('注册成功');
    router.push('/');
  } catch (error) {
    // 设置错误提醒
    console.log(error.response.data)
    let data = error.response.data
    let mes = ""
    for (let key in data){
      mes = data[key][0]
    }
        message.error(mes)
  }
}


</script>

<template>
  <div class="box">
    <img src="../../static/image/Loginbg.3377d0c.jpg" alt="">
    <div class="register">
      <div class="register_box">
        <div class="register-title">注册路飞学城</div>
        <div class="inp">
          <input v-model="mobile" type="text" placeholder="手机号码" class="user">
          <input v-model="password" type="password" placeholder="登录密码" class="user">
          <input v-model="sms_code" type="text" placeholder="输入验证码" class="user">

          <div id="geetest"></div>
          <button class="register_btn" @click="registerHandler">注册</button>
          <p class="go_login">已有账号
            <router-link to="/user/login">直接登录</router-link>
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

.box .register {
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

.register .register-title {
  width: 100%;
  font-size: 24px;
  text-align: center;
  padding-top: 30px;
  padding-bottom: 30px;
  color: #4a4a4a;
  letter-spacing: .39px;
}

.register-title img {
  width: 190px;
  height: auto;
}

.register-title p {
  font-family: PingFangSC-Regular;
  font-size: 18px;
  color: #fff;
  letter-spacing: .29px;
  padding-top: 10px;
  padding-bottom: 50px;
}

.register_box {
  width: 400px;
  height: auto;
  background: #fff;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, .5);
  border-radius: 4px;
  margin: 0 auto;
  padding-bottom: 40px;
}

.register_box .title {
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

.register_box .title span:nth-of-type(1) {
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

.register_btn {
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