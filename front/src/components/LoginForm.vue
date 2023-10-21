<template>
  <a-typography-title :level="2">Welcome to CSV service!</a-typography-title>
  <a-form
    :model="formState"
    name="basic"
    :label-col="{ span: 8 }"
    :wrapper-col="{ span: 24 }"
    autocomplete="off"
    @finish="onFinish"
    @finishFailed="onFinishFailed"
  >
    <a-form-item name="email" :rules="[{ required: true, message: 'Please input your email!' }]">
      <a-input v-model:value="formState.email" placeholder="Input your email" :disabled="loaded" />
    </a-form-item>

    <a-form-item
      name="password"
      :rules="[{ required: true, message: 'Please input your password!' }]"
    >
      <a-input-password
        v-model:value="formState.password"
        placeholder="Input your password"
        :disabled="loaded"
      />
    </a-form-item>
    <a-form-item :wrapper-col="{ span: 24 }">
      <a-button type="primary" html-type="submit" class="submitButton" :loading="loaded"
        >Submit</a-button
      >
    </a-form-item>
  </a-form>
</template>
<script lang="ts">
import { defineComponent, reactive } from 'vue'
import { useUserStore } from '../stores/user'
import router from '../router/index'
import { message } from 'ant-design-vue'
interface FormState {
  email: string
  password: string
  remember: boolean
}
export default defineComponent({
  data() {
    return {
      loaded: false,
    }
  },
  setup() {
    const formState = reactive<FormState>({
      email: '',
      password: '',
      remember: true,
    })

    return {
      formState,
    }
  },
  methods: {
    async onFinish(values: any) {
      this.loaded = true
      await new Promise((r) => setTimeout(r, 1000))
      const user = useUserStore()
      user.login(values.email, values.password).then((res) => {
        if (!res) {
          message.error('Login error, try again')
          console.log('Error')
          this.loaded = false
        }
      })
    },
    onFinishFailed(errorInfo: any) {
      console.log('Failed:', errorInfo)
      message.error('Fill all fields and try again')
    },
  },
})
</script>

<style>
.submitButton {
  width: 100%;
}
</style>
