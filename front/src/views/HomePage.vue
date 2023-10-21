<template>
  <a-layout style="min-height: 100vh">
    <a-layout>
      <a-layout-header style="background: #fff; padding: 0">
        <a-row :wrap="true">
          <a-col flex="auto">
            <HeaderTitle />
          </a-col>
          <a-col flex="100px">
            <LogoutButton />
          </a-col>
        </a-row>
      </a-layout-header>

      <a-layout-content style="margin: 0 16px">
        <a-breadcrumb style="margin: 16px 0"> </a-breadcrumb>
        <div :style="{ padding: '24px', background: '#fff', minHeight: 'calc(100vh - 150px)' }">
          <RouterView />
        </div>
      </a-layout-content>
      <a-layout-footer style="text-align: center"> Dubina Dmitry 2023 </a-layout-footer>
    </a-layout>
  </a-layout>
</template>
<script lang="ts">
import { defineComponent, ref } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import { useUserStore } from '../stores/user'
import { storeToRefs } from 'pinia'
import LogoutButton from '../components/LogoutButton.vue'
import HeaderTitle from '../components/HeaderTitle.vue'
export default defineComponent({
  components: {
    LogoutButton,
    HeaderTitle,
  },
  data() {
    return {
      collapsed: ref<boolean>(false),
      selectedKeys: ref<string[]>(['1']),
      openKeys: ref<string[]>(['1']),
    }
  },
  setup() {},
  created() {},
  async mounted() {},
  methods: {},
})
</script>
<style>
.ant-layout-sider-trigger {
  /* posi !important; */
}

.components-layout-demo-side .logo {
  height: 32px;
  margin: 16px;
  background: rgba(255, 255, 255, 0.3);
}

.site-layout .site-layout-background {
  background: #fff;
}

[data-theme='dark'] .site-layout .site-layout-background {
  background: #141414;
}

.menuItem {
  color: white;
}
</style>
