<template>
  <div>
    <a-row justify="center">
      <a-col
        class="colFile"
        :xs="{ span: 24 }"
        :sm="{ span: 12 }"
        :md="{ span: 12 }"
        :lg="{ span: 8 }"
        :xl="{ span: 8 }"
        :xxl="{ span: 6 }"
        :xxxl="{ span: 6 }"
      >
        <a-upload-dragger
          v-model:fileList="fileList"
          name="file"
          :customRequest="
            async (data: any) => {
              await file.createFile(data)
              uploaded = true
              await update()
            }
          "
          class="appendFileCard"
          multiple="false"
          :showUploadList="false"
          :before-upload="beforeUpload"
          :after-upload="afterUpload"
          :disabled="!uploaded"
          accept="text/csv"
        >
          <p class="ant-upload-text">Click or drag file to this area to upload</p>
          <loading-outlined v-if="!uploaded" class="icon" />
          <cloud-upload-outlined v-if="uploaded" class="icon" />
        </a-upload-dragger>
      </a-col>

      <a-col
        class="colFile"
        v-for="item in dataSource"
        :key="item.id"
        :xs="{ span: 24 }"
        :sm="{ span: 12 }"
        :md="{ span: 12 }"
        :lg="{ span: 8 }"
        :xl="{ span: 8 }"
        :xxl="{ span: 6 }"
        :xxxl="{ span: 6 }"
      >
        <router-link :to="uploaded ? { path: item.id } : {}" append>
          <a-card :hoverable="uploaded" :title="item.name" class="fileCard">
            <p>Columns count: {{ item.columns.length }}</p>
            <p>
              Columns names:
              <template v-for="obj in item.columns">
                <a-tag>{{ obj }}</a-tag>
              </template>
            </p>
            <p>
              Columns types:
              <template v-for="obj in item.types">
                <a-tag>{{ obj }}</a-tag>
              </template>
            </p>
            <p>Rows count: {{ item.rows }}</p>
          </a-card>
        </router-link>
      </a-col>
    </a-row>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { useFileStore } from '../stores/file'
import { type IFile } from '../api/file'
import { type IUser } from '../api/user'
import { ref } from 'vue'
import { CloudUploadOutlined, LoadingOutlined } from '@ant-design/icons-vue'
import type { UploadProps } from 'ant-design-vue'
import { useUserStore } from '@/stores/user'

export default defineComponent({
  components: {
    CloudUploadOutlined,
    LoadingOutlined,
  },
  data() {
    return {
      dataSource: [] as IFile[] | null,
      loaded: false,
      uploaded: true,
    }
  },
  setup() {
    const file = useFileStore()
    const user = useUserStore()
    const fileList = ref<UploadProps['fileList']>([])
    const uploading = ref<boolean>(false)
    return {
      file,
      fileList,
      uploading,
      user,
    }
  },
  created() {},
  async mounted() {
    this.file.requestFiles()
    this.dataSource = this.file.getFiles
    this.loaded = true
  },
  methods: {
    async update() {
      this.file.requestFiles()
      this.dataSource = this.file.getFiles
      this.loaded = true
    },
    async beforeUpload(file: any) {
      this.uploaded = false
    },
    async afterUpload(file: any) {
      this.uploaded = true
    },
  },
})
</script>
<style>
.headerButton {
  width: 80%;
}

.fileCard {
  width: 100%;
  height: 100%;
  min-width: 200px;
}

.appendFileCard {
  text-align: center;
  width: 100% !important;
  height: 100%;
  min-width: 200px;
  min-height: 300px;
}

.colFile {
  padding: 15px;
}

.icon {
  font-size: 6em;
}
</style>
