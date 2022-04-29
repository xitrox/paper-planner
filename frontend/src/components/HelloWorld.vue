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
      days,
      daysPerWeek,
      hoursPerDay,
    };
  },
};
</script>

<template>
  <div>
    <label>Days per week</label>
    <q-select
      :options="days"
      v-model="daysPerWeek"
      :model-value="daysPerWeek"
      label="Days per week"
    ></q-select>
    <br />
    <label>Hours per day</label>
    <q-slider
      class="q-mt-lg"
      :max="8"
      marker-labels
      label-always
      v-model="hoursPerDay"
      >Test</q-slider
    >

    <!-- <button @click="post">POST</button> -->

    <q-form @submit="post" class="q-gutter-md">
      <q-input filled v-model="title" label="Paper Title" />
      <q-input filled v-model="author" label="author" />
      <q-input filled v-model="journal" label="journal" />
      <q-input filled v-model="date" label="date" />
      <q-input filled v-model="pages" label="pages" />

      <div>
        <q-btn label="Submit" type="submit" color="primary" />
      </div>
    </q-form>

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
