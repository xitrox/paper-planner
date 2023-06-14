<template>
  <q-layout view="hHh lpR fFf">
    <q-header elevated class="bg-primary text-white" height-hint="98">
      <q-toolbar>
        <q-toolbar-title>
          <q-avatar>
            <img src="https://cdn.quasar.dev/logo-v2/svg/logo-mono-white.svg" />
          </q-avatar>
          Title
        </q-toolbar-title>
      </q-toolbar>

      <q-tabs align="left">
        <q-route-tab name="mails" icon="library_add" label="Add Journal" to="/" />
        <q-route-tab name="literature" icon="book" label="Literature" to="/literature" />
        <q-route-tab name="alarms" icon="info" label="About" to="/about" />
      </q-tabs>
    </q-header>



    <q-page-container>
      <q-page padding>
        <router-view />
      </q-page>
    </q-page-container>

    <!-- <div class="row">
      <div class="col-3">1</div>
      <div class="col"> <router-view /></div>
      <div class="col-3">1</div>
    </div> -->



    <q-footer elevated class="bg-grey-8 text-white">
      <q-toolbar>
        <q-toolbar-title>
          <q-avatar>
            <img src="https://cdn.quasar.dev/logo-v2/svg/logo-mono-white.svg" />
          </q-avatar>
          <div>Title</div>
        </q-toolbar-title>
      </q-toolbar>
    </q-footer>
  </q-layout>
</template>


<script>
import { ref } from "vue";

export default {
  setup() {
    return {};
  },
};
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
