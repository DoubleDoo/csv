import axios from 'axios'
import { Config } from '../config'
import { useUserStore } from '@/stores/user'

const API_URL = Config.SERVER_URL
const API_PATH = 'user'
const API_PATH_PASSWORD = 'password'

export type IUserPasswordChange = {
  newPassword: string
  oldPassword: string
}

export type IUser = {
  id: string
  name: string
  surname: string
  email: string
  role: string
}

export type IUserCreate = {
  name: string
  surname: string
  email: string
  password: string
}

export type IUserUpdate = {
  name?: string
  surname?: string
}

export const api_getUsers = async () => {
  return axios
    .get(`${API_URL}/${API_PATH}`, {
      headers: { Authorization: `Bearer ${useUserStore().getToken}` },
    })
    .then(function (response) {
      return response.data as IUser[]
    })
    .catch(function (error) {
      console.log(error)
      return null
    })
}

export const api_getUser = async (id: string) => {
  return axios
    .get(`${API_URL}/${API_PATH}/` + id, {
      headers: { Authorization: `Bearer ${useUserStore().getToken}` },
    })
    .then(function (response) {
      return response.data as IUser
    })
    .catch(function (error) {
      console.log(error)
      return null
    })
}

export const api_postUser = async (obj: IUserCreate) => {
  return axios
    .post(`${API_URL}/${API_PATH}`, obj, {
      headers: { Authorization: `Bearer ${useUserStore().getToken}` },
    })
    .then(function (response) {
      return response.data as IUser
    })
    .catch(function (error) {
      console.log(error)
      return null
    })
}

export const api_putUser = async (id: string, obj: IUserUpdate) => {
  return axios
    .put(`${API_URL}/${API_PATH}/` + id, obj, {
      headers: { Authorization: `Bearer ${useUserStore().getToken}` },
    })
    .then(function (response) {
      return response.data as IUser
    })
    .catch(function (error) {
      console.log(error)
      return null
    })
}

export const api_putUserPassword = async (id: string, obj: IUserPasswordChange) => {
  return axios
    .put(`${API_URL}/${API_PATH_PASSWORD}/` + id, obj, {
      headers: { Authorization: `Bearer ${useUserStore().getToken}` },
    })
    .then(function (response) {
      return response.data as IUser
    })
    .catch(function (error) {
      console.log(error)
      return null
    })
}

export const api_deleteUser = async (id: string) => {
  return axios
    .delete(`${API_URL}/${API_PATH}/` + id, {
      headers: { Authorization: `Bearer ${useUserStore().getToken}` },
    })
    .then(function (response) {
      return response
    })
    .catch(function (error) {
      console.log(error)
      return null
    })
}
