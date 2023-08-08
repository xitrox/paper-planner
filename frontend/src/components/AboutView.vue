<script>
import { onMounted, ref } from "vue";
import { useQuasar } from "quasar";
import { usePhasesStore } from '../store/phases';

export default {
  setup() {
    const $q = useQuasar();
    const phasesStore = usePhasesStore();
    const phases = ref([]);

    // Use ref to track whether the data has been fetched
    const isDataFetched = ref(false);

    // Fetch data on component mount
    onMounted(async () => {
      await phasesStore.fetchPhases();
      console.log(phasesStore.phases)
      phases.value = phasesStore.phases;
      isDataFetched.value = true; // Update the fetched status

    });

    // Expose to template and other options API hooks
    return {
      phases,
      isDataFetched, // Expose the fetched status
    };
  },
};

</script>


<template>
  <div>
    <h1>Authors: Die Tobis</h1>
  </div>

  <div>
    <h1>Phases</h1>
    <ul v-if="isDataFetched">
      <li v-for="phase in phases" :key="phase.phase_name">
        {{ phase.phase_name }}
      </li>
    </ul>
    <p v-else>Loading phases...</p>
  </div>
</template>


