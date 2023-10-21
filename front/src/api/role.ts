import axios from 'axios'
import { useUserStore } from '../stores/user'
import { Config } from '../config'

const API_URL = Config.SERVER_URL
const API_PATH = 'role'

export const api_getRoles = async () => {
  return axios
    .get(`${API_URL}/${API_PATH}`, {
      headers: { Authorization: `Bearer ${useUserStore().getToken}` },
    })
    .then(function (response) {
      return response.data as string[]
    })
    .catch(function (error) {
      console.log(error)
      return null
    })
}
