<script setup>
import {ref, onMounted, inject, computed} from 'vue'
import {useMessage} from "naive-ui"

const nav_list = ref([]);
const axios = inject('axios');
const settings = inject('settings');
const message = useMessage();
const userToken = ref("")

const options = [
  {
    label: "我的账户",
    key: "marina bay sands",

  },
  {
    label: "我的订单",
    key: "brown's hotel, london"
  },
  {
    label: "我的优惠券",
    key: "atlantis nahamas, nassau"
  },
  {
    label: "退出登录",
    key: "退出登录",
  }
];
const checkUserLoginStatus = () => {
  return localStorage.getItem('user_access_token') || sessionStorage.getItem('user_access_token');
};
const logout = () =>{
   // 执行退出登录操作
    localStorage.removeItem('refresh_token');
    localStorage.removeItem('user_id');
    localStorage.removeItem('user_name');
    localStorage.removeItem('user_access_token');
    sessionStorage.removeItem('user_access_token');
    userToken.value = ""; // 清空用户令牌
    message.success("已退出登录");
};
const handleSelect = (key) => {
  if (key === "退出登录") {
   logout();
  }
};

// 在组件挂载后进行 AJAX 请求
onMounted(async () => {
     userToken.value = checkUserLoginStatus();
      try {
        // 请求标题
        const response = await axios.get(`${settings.HOST}/nav/header/`);
        nav_list.value = response.data;
      } catch (error) {
        console.error(error);
      }
    }
);

const isUserLoggedIn = computed(() => !!userToken.value);
</script>
<template>
  <div class="header-box">
    <div class="header">
      <div class="content">
        <div class="logo full-left">
          <router-link to="/"><img src="/static/image/logo.svg" alt=""></router-link>
        </div>
        <ul class="nav full-left">
          <li v-for="nav in nav_list">
            <span v-if="nav.is_site"><a :href="nav.link">{{ nav.title }}</a></span>
            <span v-else><router-link :to="nav.link">{{ nav.title }}</router-link></span>
          </li>
        </ul>


        <div v-if="isUserLoggedIn" class="login-bar full-right">
          <div class="shop-cart full-left">
            <span class="shop-cart-total"></span>
            <img src="/static/image/cart.svg" alt="">
            <span><router-link to="/cart">购物车</router-link></span>
          </div>
          <div class="login-bar full-right login-box ">
            <n-dropdown trigger="hover" :options="options" @select="handleSelect">
              <router-link to="">
                <n-button>学习中心</n-button>
              </router-link>
            </n-dropdown>
          </div>
        </div>


        <div v-else class="login-bar full-right">
          <div class="shop-cart full-left">
            <img src="/static/image/cart.svg" alt="">
            <span><router-link to="/cart">购物车</router-link></span>
          </div>
          <div class="login-box full-left">
            <router-link to="/user/login">登录</router-link>
            &nbsp;|&nbsp;
             <router-link to="/user/register">注册</router-link>
          </div>
        </div>

      </div>
    </div>
  </div>

</template>

<style scoped>
.header-box {
  height: 80px;
}

.header {
  width: 100%;
  height: 80px;
  box-shadow: 0 0.5px 0.5px 0 #ffffff;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  margin: auto;
  z-index: 99;
  background: #ffffff;
}

.header .content {
  max-width: 1200px;
  width: 100%;
  margin: 0 auto;
}

.header .content .logo {
  height: 80px;
  line-height: 80px;
  margin-right: 50px;
  cursor: pointer; /* 设置光标的形状为爪子 */
}

.header .content .logo img {
  vertical-align: middle;
}

.header .nav li {
  float: left;
  height: 80px;
  line-height: 80px;
  margin-right: 30px;
  font-size: 16px;
  color: #4a4a4a;
  cursor: pointer;
}

.header .nav li span {
  padding-bottom: 16px;
  padding-left: 5px;
  padding-right: 5px;
}

.header .nav li span a {
  display: inline-block;
}

.header .nav li .this {
  color: #4a4a4a;
  border-bottom: 4px solid #ffc210;
}

.header .nav li:hover span {
  color: #000;
}

.header .login-bar {
  height: 80px;
}

.header .login-bar .shop-cart {
  margin-right: 20px;
  border-radius: 17px;
  background: #f7f7f7;
  cursor: pointer;
  font-size: 14px;
  height: 28px;
  width: 90px;
  margin-top: 30px;
  line-height: 32px;
  text-align: center;
}

.member {
  display: inline-block;
  height: 34px;
  margin-left: 20px;
}

.member img {
  width: 26px;
  height: 26px;
  border-radius: 50%;
  display: inline-block;
}

.member img:hover {
  border: 1px solid yellow;
}

.header .login-bar .login-box1 {
  margin-top: 16px;
}

.drop_menu {
  margin-right: 20px;
  border-radius: 17px;
  background: #ffffff;
  cursor: pointer;
  font-size: 16px;
  height: 28px;
  width: 88px;
  margin-top: 30px;
  line-height: 32px;
  text-align: center;
}

.header .login-bar .shop-cart:hover {
  background: #f0f0f0;
}

.header .login-bar .shop-cart img {
  width: 15px;
  margin-right: 4px;
  margin-left: 6px;
}

.header .login-bar .shop-cart span {
  margin-right: 6px;
}

.header .login-bar .login-box {
  margin-top: 33px;
}

.header .login-bar .login-box span {
  cursor: pointer;
}

.header .login-bar .login-box span:hover {
  color: rgb(0, 128, 0);
}

.n-button {
  margin: -6px
}
</style>