import { defineStore, acceptHMRUpdate } from 'pinia'
import {
  api_deleteFile,
  api_getFile,
  api_getFiles,
  api_postFile,
  type IFile,
  type IFilePageRequest,
} from '../api/file'
import { message } from 'ant-design-vue'

export interface fileStoreState {
  files: IFile[] | null
  curentFile: IFile | null
  curentFileData: any[] | null
}

export const useFileStore = defineStore({
  id: 'unit',
  state: (): fileStoreState => ({
    files: null,
    curentFile: null,
    curentFileData: null,
  }),
  persist: {
    storage: sessionStorage,
  },
  getters: {
    getFiles(state) {
      return state.files
    },
    getFileById(state) {
      return (id: string) => state.files!.find((obj) => obj.id === id)
    },
    getCurentFile(state) {
      return () => state.curentFile
    },
    getCurentFileData(state) {
      return () => state.curentFileData
    },
  },
  actions: {
    async createFile(data: any) {
      await api_postFile(data).then((res) => {
        if (res && this.files != null) {
          this.files.push(res)
          message.success('File upload success')
        } else {
          message.error('File upload error')
        }
      })
    },
    async requestFiles() {
      await api_getFiles().then((res) => {
        if (res) {
          this.files = res
        }
      })
    },
    async requestFile(id: string, obj: IFilePageRequest) {
      await api_getFile(id, obj).then((res) => {
        if (res) {
          this.curentFile = res.file
          this.curentFileData = res.data
        }
      })
    },
    async deleteFile(id: string) {
      await api_deleteFile(id).then((res) => {
        if (res) {
          this.files = this.files!.filter((value) => {
            return value.id != id
          })
        } else {
          message.error('File delete error')
        }
      })
    },
  },
})

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useFileStore, import.meta.hot))
}
