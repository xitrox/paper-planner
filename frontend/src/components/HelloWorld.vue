<script>
import { onMounted, ref } from "vue";
import axios from "axios";
import { useQuasar } from "quasar";

export default {
  setup() {
    const $q = useQuasar();
    const count = ref(0);
    const posts = ref([]);
    const title = ref(null);
    const author = ref(null);
    const journal = ref(null);
    const date = ref(null);
    const pages = ref(null);

    const fetchData = () => {
      axios
        .get(`http://localhost:8000/paper/`)
        .then((response) => {
          // JSON responses are automatically parsed.
          console.log(response.data);
          posts.value = response.data;
        })
        .catch((e) => {
          this.errors.push(e);
        });
    };

    onMounted(() => {
      fetchData();
    });

    const post = () => {
      axios
        .post(`http://localhost:8000/paper/`, {
          title: title.value,
          author: author.value,
          journal: journal.value,
          date: date.value,
          pages: pages.value,
        })
        .then((response) => {
          fetchData();
        })
        .catch((e) => {
          this.errors.push(e);
        });
    };

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
      post,
      removePost,
      title,
      author,
      journal,
      date,
      pages,
    };
  },
};
</script>

<template>
  <div>
    <q-form @submit="post">
      <q-input v-model="title" label="Title"></q-input>
      <q-input v-model="author" label="Author"></q-input>
      <q-input v-model="journal" label="Journal"></q-input>
      <q-input v-model="date" label="Date"></q-input>
      <q-input v-model="pages" label="Pages "></q-input>
      <q-btn label="Submit" type="submit" color="primary"></q-btn>
    </q-form>
    <!--/* <button @click="post">POST</button> */ -->
    <div v-for="(post, index) in posts" :key="post.id">
      {{ post.id }}: {{ post.title }}
      <button color="blue" @click="removePost(index, post.id)">delete</button>
    </div>

    <p>
      Edit
      <code>components/HelloWorld.vue</code> to test hot module replacement.
    </p>
  </div>
</template>

<style scoped>
a {
  color: #42b983;
}
</style>
