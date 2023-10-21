import { defineStore, acceptHMRUpdate } from 'pinia'
import { api_getRoles } from '../api/role'

export const useRoleStore = defineStore({
  id: 'role',
  state: () => ({
    roles: {} as string[],
  }),
  persist: {
    storage: sessionStorage,
  },
  getters: {
    getRoles(state) {
      return state.roles
    },
  },
  actions: {
    async requestRoles() {
      await api_getRoles().then((res) => {
        if (res) {
          this.roles = res
        }
      })
    },
  },
})

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useRoleStore, import.meta.hot))
}
