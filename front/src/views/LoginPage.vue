<template>
  <div class="loginBox">
    <LoginForm />
  </div>
</template>

<script lang="ts">
import LoginForm from '../components/LoginForm.vue'
import { defineComponent, ref } from 'vue'
export default defineComponent({
  components: {
    LoginForm,
  },
  data() {},
})
</script>

<style>
.loginBox {
  position: absolute;
  width: 500px;
  top: 50%;
  left: 50%;
  margin-right: -50%;
  transform: translate(-50%, -50%);
}
</style>
