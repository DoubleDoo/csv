import axios from 'axios'
import { Config } from '../config'
import type { IUser } from './user'

const API_URL = Config.SERVER_URL
const API_PATH = 'auth'

export type IAuthRequest = {
  email: string
  password: string
}

export type IAuthUser = {
  token: string
  user: IUser
}

export const api_login = async (data: IAuthRequest) => {
  return axios
    .post(`${API_URL}/${API_PATH}`, data, {
      headers: {
        'Content-Type': 'application/json',
        'Referrer-Policy': 'origin',
      },
    })
    .then(function (response) {
      return response.data as IAuthUser
    })
    .catch(function (error) {
      console.log(error)
      return null
    })
}
