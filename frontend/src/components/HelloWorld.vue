<script>
import { ref } from "vue";
import axios from "axios";

export default {
  setup() {
    const count = ref(0);
    const posts = ref([]);

    const post = () => {
      axios
        .post(`http://localhost:8000/paper/`, {
          title: "test",
          author: "die Tobis",
          journal: "WICHTIG Daily",
          date: "2022",
          pages: "200-300",
        })
        .then((response) => {})
        .catch((e) => {
          this.errors.push(e);
        });
    };

    const removePost = (postId) => {
      console.log(postId);
      posts.value.splice(postId, 1);
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
    };
  },

  mounted() {
    axios
      .get(`http://localhost:8000/paper/`)
      .then((response) => {
        // JSON responses are automatically parsed.
        console.log(response.data);
        this.posts = response.data;
      })
      .catch((e) => {
        this.errors.push(e);
      });
  },
};
</script>

<template>
  <div>
    <p>
      Recommended IDE setup:
      <a href="https://code.visualstudio.com/" target="_blank">VSCode</a>
      +
      <a href="https://github.com/johnsoncodehk/volar" target="_blank">Volar</a>
    </p>
    <p>
      <a href="https://vitejs.dev/guide/features.html" target="_blank">
        Vite Documentation
      </a>
      |
      <a href="https://v3.vuejs.org/" target="_blank">Vue 3 Documentation</a>
    </p>
    <button @click="post">POST</button>
    <div v-for="post in posts" :key="post.id">
      {{ post.id }}: {{ post.title }}
      <button color="blue" @click="removePost(post.id)">delete</button>
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
