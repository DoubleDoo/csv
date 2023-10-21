<template>
  <a-button @click="handleClick" type="primary" danger class="headerButton">Logout</a-button>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { useUserStore } from '../stores/user'
export default defineComponent({
  components: {},
  setup() {
    const user = useUserStore()
    const handleClick = (evt: Event) => {
      user.logout()
      // router.push({ path: '/login' });ur
    }
    return { handleClick }
  },
})
</script>
<style>
.headerButton {
  width: 80%;
}
</style>
