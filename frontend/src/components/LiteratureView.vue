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
      { name: "title", label: "Title", field: "title" },
      { name: "author", label: "Author", field: "author" },
      { name: "pages", label: "Pages", field: "pages" },
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

    const removePost = (index, postId) => {
      console.log(postId);
      posts.value.splice(index, 1);
      console.log(posts.value);
      axios.delete("http://localhost:8000/paper/" + postId).then((response) => {
        console.log(response);
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
  <q-table
    v-if="!loading"
    title="Journals"
    :rows="posts"
    :columns="columns"
    row-key="name"
  />
  <!-- <div>
    <div v-for="(post, index) in posts" :key="post.id">
      {{ post.id }}: {{ post.title }}
      <button color="blue" @click="removePost(index, post.id)">delete</button>
      <h1>Hallo Hallo test</h1>
    </div>
  </div> -->
</template>

<style scoped>
a {
  color: #42b983;
}
</style>
