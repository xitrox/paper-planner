<script>
import { onMounted, ref } from "vue";
import axios from "axios";
import { useQuasar } from "quasar";

export default {
  setup() {
    const $q = useQuasar();
    const count = ref(0);
    const posts = ref([]);
    const loading = ref(true);
    const columns = [
      { name: 'title', label: 'Title', field: 'title' },
      { name: 'author', label: 'Author', field: 'author' },
      { name: 'pages', label: 'Pages', field: 'pages' },
      { name: 'delete', field: 'delete', label: 'Action' }

    ];

    const days = ["1", "2", "3", "4", "5", "6", "7"];
    const daysPerWeek = ref(null);
    const hoursPerDay = ref(0);

    const fetchData = () => {
      axios
        .get(`http://localhost:8000/paper/`)
        .then((response) => {
          // JSON responses are automatically parsed.
          console.log(response.data);
          posts.value = response.data;
          loading.value = false;
        })
        .catch((e) => {
          this.errors.push(e);
        });
    };

    onMounted(() => {
      fetchData();
    });

    const removePost = (postId) => {
      console.log(postId);
      axios.delete("http://localhost:8000/paper/" + postId).then((response) => {
        console.log(response);
        fetchData();
      });
    };

    // expose to template and other options API hooks
    return {
      posts,
      count,
      removePost,
      columns,
      loading,
    };
  },
};
</script>

<template>
  <q-table v-if="!loading" title="Journals" :rows="posts" :columns="columns" :pagination="{ rowsPerPage: 10 }"
    row-key="name">
    <template v-slot:body="props">
      <q-tr :props="props">
        <q-td key="title" :props="props">
          {{ props.row.title }}
        </q-td>
        <q-td key="author" :props="props">
          {{ props.row.author }}
        </q-td>
        <q-td key="pages" :props="props">
          {{ props.row.pages }}
        </q-td>
        <q-td key="delete" :props="props">
          <q-icon size="md" name="delete" @click="removePost(props.row.id)" />
        </q-td>
      </q-tr>
    </template>
  </q-table>
</template>

    <style scoped>
    a {
      color: #42b983;
    }
    </style>
