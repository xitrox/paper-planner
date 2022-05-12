<template>
  <div>Toller header</div>

  <div class="q-pa-md">
    <div class="q-gutter-y-md" style="max-width: 600px">
      <q-tabs v-model="tab" class="text-teal">
        <q-route-tab name="mails" icon="mail" label="Mails" to="/" />
        <q-route-tab name="alarms" icon="alarm" label="Alarms" to="/about" />
        <q-tab name="movies" icon="movie" label="Movies" />
      </q-tabs>
    </div>
  </div>

  <router-link to="/">Main</router-link><br />
  <router-view></router-view>
</template>

<script setup>
import { ref } from "vue";
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup
const tab = ref("movies");
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
