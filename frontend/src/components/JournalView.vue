<script>
import { onMounted, ref } from "vue";
import axios from "axios";
import { useQuasar } from "quasar";
import LiteratureView from "./LiteratureView.vue";


export default {

  components: {
    LiteratureView,
  },
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
        .get(`http://localhost:8000/bibliography/paper/`)
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

    const showNotification = (message) => {
      $q.notify({ message: message, icon: "fact_check" })
    }

    const post = () => {
      axios
        .post(`http://localhost:8000/bibliography/paper/`, {
          title: title.value,
          author: author.value,
          journal: journal.value,
          date: date.value,
          pages: pages.value,
        })
        .then((response) => {
          fetchData();
          title.value = "";
          author.value = "";
          journal.value = "";
          date.value = "";
          pages.value = "";
        })
        .catch((e) => {
          console.log(e);
          this.errors.push(e);
        });
    };

    // expose to template and other options API hooks
    return {
      posts,
      count,
      post,
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
  <div class="q-px-lg">
    <label>Days per week</label>
    <q-select :options="days" v-model="daysPerWeek" :model-value="daysPerWeek" label="Days per week"></q-select>
    <br />
    <label>Hours per day</label>
    <q-slider class="q-mt-lg" :max="8" marker-labels label-always v-model="hoursPerDay">Test</q-slider>

    <q-form @submit="post" class="q-gutter-md">
      <q-input filled v-model="title" label="Paper Title" />
      <q-input filled v-model="author" label="author" />
      <q-input filled v-model="journal" label="journal" />
      <q-input filled v-model="date" label="date" />
      <q-input filled v-model="pages" label="pages" />

      <div>
        <q-btn label="Add to Journal" type="submit" color="primary" />
      </div>
    </q-form>


    <br>

    <div class="q-px-lg">
      <LiteratureView></LiteratureView>
    </div>


  </div>
</template>

<style scoped>
a {
  color: #ae2a2a;
}
</style>
