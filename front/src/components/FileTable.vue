<template>
  <a-button type="primary" class="actionbutton" @click="$router.replace('/')">Back</a-button>
  <a-button
    v-if="user.isAdmin"
    type="primary"
    class="actionbutton"
    danger
    @click="
      async () => {
        await file.deleteFile(id)
        $router.replace('/')
      }
    "
    >Delete</a-button
  >
  <a-table
    sticky
    :columns="columns"
    :data-source="dataSource"
    :scroll="{ x: columns.length * 150 }"
    :pagination="false"
    :scrollToFirstRowOnChange="true"
    :onChange="onChange"
  >
    <template #bodyCell="{ column, record }">
      <div v-if="column.dataIndex">
        <div v-if="!loaded">
          <a-skeleton-input active class="loadRow" />
        </div>
        <div v-else>
          <div class="dataRow">
            {{ record[column.title] }}
          </div>
        </div>
      </div>
    </template>
  </a-table>
  <a-row>
    <a-col :span="24" class="paginationRow">
      <a-pagination
        :total="size"
        :pageSizeOptions="[10, 50, 100]"
        :current="currentPage"
        class="pagination"
        :onChange="pageChange"
      />
    </a-col>
  </a-row>
</template>

<script lang="ts">
import { type IFile, type ISort } from '../api/file'
import { defineComponent } from 'vue'
import { useFileStore } from '../stores/file'
import { useRoute } from 'vue-router'
import { api_getFile } from '../api/file'
import { useUserStore } from '@/stores/user'

type ICoulmn = {
  title: string
  dataIndex: string
  width: string
}

export default defineComponent({
  data() {
    return {
      dataSource: [] as any[],
      loaded: false,
      currentPage: 1,
      pageSize: 10,
      size: 10,
      sort:[] as ISort[]
    }
  },
  setup() {
    console.log('created')
    const file = useFileStore()
    const user = useUserStore()
    const route = useRoute()
    const id = route.params.fileUUID.toString()
    const pickerd = file.getFileById(id)

    let buf = [] as any[]
    if (pickerd != undefined) buf = pickerd.columns
    buf = buf.map((element: string) => {
      return {
        title: element,
        dataIndex: element,
        width: '100%',
        ellipsis: true,
        sorter: true,
      }
    })
    const columns = buf
    console.log(columns)
    const curentfile = file.curentFile
    return {
      id,
      file,
      columns,
      curentfile,
      user,
    }
  },
  created() {
    const buf = [] as any[]
    for (let i = 0; i < 10; i++) {
      buf.push({})
    }
    this.dataSource = buf
  },
  async mounted() {
    await this.update()
  },
  methods: {
    async update() {
      this.loaded = false
      await this.file.requestFile(this.id, {
        page: this.currentPage - 1,
        size: this.pageSize,
        sort: this.sort,
      })
      if (this.file.curentFile!= null) this.size = this.file.curentFile.rows
      if (this.file.curentFileData != null) this.dataSource = this.file.curentFileData
      this.loaded = true
    },
    async pageChange(page: any, pageSize: any) {
      this.currentPage = page
      this.pageSize = pageSize
      this.update()
    },
    async sortChange(dta: any) {
      this.update()
    },
    async onChange(pagination: any, filters: any, sorter: any, extra: any) {
      this.sort = []
      if (sorter.column != undefined)
        this.sort.push({
          column: sorter.column.title,
          dirrection: sorter.order,
        })
      await this.update()
    },
  },
  components: {},
})
</script>
<style scoped>
.actionbutton {
  width: 150px;
  margin-right: 20px;
  margin-bottom: 20px;
}

.pagination {
  margin-top: 50px;
}

.paginationRow {
  align-content: right;
  text-align: right;
}

.loadRow{
  height: 25px;
}

.dataRow{
  height: 25px;
}
</style>
