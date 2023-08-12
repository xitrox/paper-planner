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
            phases.value = phasesStore.phases.filter(phase => phase.phase_name === "Einarbeitung");

            isDataFetched.value = true; // Update the fetched status

        });


        // Expose to template and other options API hooks
        return {
            phases,
            isDataFetched, // Expose the fetched status
            phasesStore,
        };
    },
};

</script>
<template>
    <div v-if="isDataFetched">
        <h3>Einarbeitungsphase</h3>
        <div class="row">
            <div class="col-3" v-for="phase in phases" :key="phase.phase_name">
                <p> {{ phase.phase_description }}</p>
                <p> Mehr Infos bei: {{ phase.phase_further_reading }}</p>
            </div>
            <div class="col-6">
                <ul v-for="phase in phases">
                    <li v-for="to_do in phase.to_do_set">
                        {{ to_do.to_do_name }}
                        {{ to_do.id }}
                        <q-btn label="Done" type="submit" color="primary" @click="phasesStore.postToDoDone(to_do.id)" />

                    </li>
                </ul>
            </div>

            <div class="col-3">Dein Reward für das Abschliesen der Phase:</div>
        </div>
    </div>
    <p v-else>Loading phases...</p>
</template>


