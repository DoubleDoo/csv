import { defineStore, acceptHMRUpdate } from 'pinia'
import router from '../router/index'
import { type IAuthUser, api_login } from '../api/auth'
import isValidJwt from '@/utils'

export interface userStoreState {
  userAuth: IAuthUser | null
}

export const useUserStore = defineStore({
  id: 'user',
  state: (): userStoreState => ({
    userAuth: null,
  }),
  persist: {
    storage: localStorage,
  },
  getters: {
    getToken(state) {
      if (state.userAuth != null) return state.userAuth.token != null ? state.userAuth!.token : null
      return null
    },
    getUserAuth(state) {
      if (state.userAuth != null) return state.userAuth.user != null ? state.userAuth!.user : null
      return null
    },
    isAdmin(state) {
      if (state.userAuth != null)
        return state.userAuth.user != null ? state.userAuth!.user.role == 'ADMIN' : false
      return false
    },
    isAuthenticated(state) {
      if (state.userAuth != null)
        return state.userAuth!.token != null ? isValidJwt(state.userAuth!.token) : false
      return false
    },
  },
  actions: {
    logout() {
      this.$patch({
        userAuth: null,
      })
      router.push({ path: '/login' })
    },
    async login(log: string, pass: string): Promise<boolean> {
      const res = await api_login({ email: log, password: pass })
      if (res) {
        this.$patch({
          userAuth: res,
        })
      }
      if (res != null) {
        router.push({ path: '/' })
        return true
      }
      return false
    },
  },
})

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useUserStore, import.meta.hot))
}

// newPassword(id: string) {
//   this.usersChanged[id].password = undefined;
// },
// validation(id: string): boolean {
//   if (validate(this.usersChanged[id])) return true;
//   message.warning('You forgot to fill all fields');
//   return false;
// },

// async createUser(id: string) {
//   const obj = this.getUsersChangedById(id);
//   await api_postUser(userToCreateDTO(undefinedtoUser(obj))).then((res) => {
//     if (res) {
//       Object.assign(this.users.filter((item) => item.id === id)[0], res);
//       delete this.usersChanged[id];
//       // message.success('User create success');
//     } else {
//       message.error('User create error');
//     }
//   });
// },
// async requestUsers() {
//   await api_getUsers().then((res) => {
//     if (res) {
//       this.$patch({
//         users: res,
//       });
//     }
//   });
// },
// async updateUser(id: string) {
//   const upd = this.getUsersChangedById(id);
//   const obj = this.getUsersById(id);
//   if (obj && upd.password != obj.password)
//     await api_putUser(userToUpdateDTO(undefinedtoUser(upd))).then((res) => {
//       if (res) {
//         this.users = this.users.map((value) => {
//           if (value.id == id) {
//             return undefinedtoUser(upd);
//           } else return value;
//         });
//         // message.success('User update success');
//       } else {
//         message.error('User update error');
//       }
//     });
//   else {
//     const obj2 = userToUpdateDTO(undefinedtoUser(upd));
//     const upd2: IUpdateUserDTONP = {
//       id: obj2.id,
//       name: obj2.name,
//       login: obj2.login,
//       role: obj2.role,
//       restaurants: obj2.restaurants,
//       email: obj2.email,
//     };
//     await api_putUser(upd2).then((res) => {
//       if (res) {
//         this.users = this.users.map((value) => {
//           if (value.id == id) {
//             return undefinedtoUser(upd);
//           } else return value;
//         });
//         // message.success('User update success');
//       } else {
//         message.error('User update error');
//       }
//     });
//   }
// },
// async deleteUser(id: string) {
//   await api_deleteUser(id).then((res) => {
//     if (res) {
//       this.$patch({
//         users: this.users.filter((value) => {
//           return value.id != id;
//         }),
//       });
//       // message.success('User delete success');
//     } else {
//       message.error('User delete error');
//     }
//   });
// },
