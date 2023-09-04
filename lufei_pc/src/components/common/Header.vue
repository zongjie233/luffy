<script setup>

</script>
<template>
  <el-header  class="header">
    <div class="container">
    <el-row type="flex" justify="space-between" align="middle">
      <el-col :span="16">
        <!-- 中间的选项 -->
        <el-menu mode="horizontal">
          <el-menu-item index="1">免费课</el-menu-item>
          <el-menu-item index="2">轻客</el-menu-item>
          <el-menu-item index="3">学位课</el-menu-item>
          <el-menu-item index="4">题库</el-menu-item>
          <el-menu-item index="5">老男孩教育</el-menu-item>
        </el-menu>
      </el-col>
      <el-col :span="4">
        <!-- 右侧的购物车和登录注册选项 -->
        <el-menu mode="horizontal">
          <el-submenu>
            <template #title>
              <i class="el-icon-shopping-cart-full"></i>
            </template>
          </el-submenu>
          <el-menu-item index="6">登录</el-menu-item>
          <el-menu-item index="7">注册</el-menu-item>
        </el-menu>
      </el-col>
    </el-row>
    </div>
  </el-header>
</template>

<style scoped>
.header {
  background-color: white;
  line-height: 60px;
  border-bottom: none;
}
.container {
  max-width: 1200px; /* 设置最大宽度 */
  margin: 0 auto; /* 水平方向居中 */
}
.el-header {
  background-color: white;
  line-height: 60px;
  border-bottom: none;
}
.el-menu--horizontal.el-menu {
    border-bottom: none;
}
.el-menu:not(.el-menu--horizontal) {
  height: 60px;
}
</style>