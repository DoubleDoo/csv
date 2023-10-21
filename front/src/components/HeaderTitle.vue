<template>
  <a-typography-title :level="5" class="headerText">{{ getName() }}</a-typography-title>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import { useUserStore } from '../stores/user'
import { storeToRefs } from 'pinia'
export default defineComponent({
  components: {},
  setup() {
    const user = useUserStore()
    const { userAuth } = storeToRefs(useUserStore())
    const getName = () => {
      return userAuth.value?.user.name
    }
    return { getName }
  },
})
</script>

<style>
.headerText {
  margin-top: 17px;
  margin-left: 15px;
  text-overflow: ellipsis;
}
</style>
