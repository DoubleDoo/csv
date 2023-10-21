import axios from 'axios'
import { Config } from '../config'
import { useUserStore } from '@/stores/user'

const API_URL = Config.SERVER_URL
const API_PATH = 'file'

export type IFile = {
  id: string
  name: string
  columns: string[]
  rows: number
  types: string[]
}

export type IFilePageRequest = {
  page: number
  size: number
  sort: ISort[]
}

export type IFilePageResponse = {
  data: any[]
  file: IFile
}

export type ISort = {
  column: string
  dirrection: string
}


export type IFileCreate = {
  name: string
}

export const api_getFiles = async () => {
  return axios
    .get(`${API_URL}/${API_PATH}`, {
      headers: {
        'Content-Type': 'application/json',
        'Referrer-Policy': 'origin',
        Authorization: `Bearer ${useUserStore().getToken}`,
      },
    })
    .then(function (response) {
      const res = response.data
      res.map((el: any) => {
        el.columns = JSON.parse(el.columns)
        el.types = JSON.parse(el.types)
        return el as File
      })
      return res as IFile[]
    })
    .catch(function (error) {
      console.log(error)
      return null
    })
}

export const api_getFile = async (id: string, obj: IFilePageRequest) => {
  return axios
    .post(`${API_URL}/${API_PATH}/` + id, obj, {
      headers: { Authorization: `Bearer ${useUserStore().getToken}` },
    })
    .then(function (response) {
      return {
        data: JSON.parse(response.data.data),
        file: {
          id: response.data.file.id,
          name: response.data.file.name,
          columns: JSON.parse(response.data.file.columns),
          rows: response.data.file.rows,
          types: JSON.parse(response.data.file.types),
        } as IFile,
      } as IFilePageResponse
    })
    .catch(function (error) {
      console.log(error)
      return null
    })
}

export const api_postFile = async (data: any) => {
  const formData = new FormData()
  formData.append('file', data.file)
  return await axios
    .post(`${API_URL}/${API_PATH}`, formData, {
      headers: {
        'Content-Type': 'application/octet-stream',
        Authorization: `Bearer ${useUserStore().getToken}`,
      },
    })
    .then(function (response) {
      return response.data as IFile
    })
    .catch(function (error) {
      console.log(error)
      return null
    })
}

export const api_deleteFile = async (id: string) => {
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
