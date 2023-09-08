<script setup>
import  {ref,onMounted,inject} from 'vue'
const banner_list = ref([]);
const axios = inject('axios');
const settings = inject('settings');
// 在组件挂载后进行 AJAX 请求
onMounted(async () => {
   try {
// 请求轮播图
    const response = await axios.get(`${settings.HOST}/banner/`);
    banner_list.value = response.data;
  } catch (error) {
    console.error(error);
  }
  }
);
</script>

<template>
  <n-carousel  autoplay show-arrow>
    <a :href="banner.link" v-for="banner in banner_list" :key="banner.id">
    <img class="carousel-img" :src= "banner.image_url">
    </a>
  </n-carousel>
</template>

<style scoped>
.carousel-img {
  width: 100%;
  height: 700px;
  object-fit: cover;
}

</style>