<script>
import { onMounted, ref } from "vue";
import { useQuasar } from "quasar";
import { usePhasesStore } from '../store/phases';

export default {
  setup() {
    const $q = useQuasar();
    const phasesStore = usePhasesStore();

    // Use ref to track whether the data has been fetched
    const isDataFetched = ref(false);

    // Fetch data on component mount
    onMounted(async () => {
      await phasesStore.fetchPhases();
      console.log(phasesStore.phases)
      isDataFetched.value = true; // Update the fetched status

    });

    // Expose to template and other options API hooks
    return {
      phases: phasesStore.phases,
      isDataFetched, // Expose the fetched status
    };
  },
};

</script>


<template>
  <div>
    <h3>Authors: Die Tobis und der Kosta</h3>
  </div>

  <div>
    <h1>Phases</h1>
    <ul v-if="phases.length > 0">
      <li v-for="phase in phases" :key="phase.phase_name">
        {{ phase.phase_name }}
      </li>
    </ul>
    <p v-else>No phases available.</p>
  </div>
</template>


