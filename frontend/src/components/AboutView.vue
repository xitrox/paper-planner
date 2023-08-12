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
    <h3>Authors: Die Tobis und der Costa</h3>
  </div>

  <div>
    <h3>Hier ein Test, der die alle geladenen Json Daten darstellt:</h3>
    <ul v-if="isDataFetched">
      <li v-for="phase in phases" :key="phase.phase_name">

        {{ phase }}

      </li>
    </ul>
    <p v-else>Loading phases...</p>
  </div>
</template>


