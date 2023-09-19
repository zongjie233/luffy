<script setup>
import  {ref,onMounted,inject} from 'vue'
const nav_list = ref([]);
const axios = inject('axios');
const settings = inject('settings');
// 在组件挂载后进行 AJAX 请求
onMounted(async () => {
   try {
    // 请求标题
    const response = await axios.get(`${settings.HOST}/nav/footer/`);
    nav_list.value = response.data;
  } catch (error) {
    console.error(error);
  }
  }
);
</script>

<template>
 <div class="footer">
      <ul>
        <li v-for="nav in nav_list">
              <span  v-if="nav.is_site"><a :href="nav.link">{{nav.title}}</a></span>
              <span v-else><router-link :to="nav.link">{{nav.title}}</router-link></span>
            </li>
      </ul>
      <p>Copyright © luffycity.com版权所有 | 京ICP备17072161号-1</p>
    </div>
</template>

<style scoped>
.footer {
  text-align: center;
}
</style>