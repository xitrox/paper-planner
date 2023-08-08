// src/store/modules/phases.js

import { defineStore } from 'pinia';
import axios from 'axios';

export const usePhasesStore = defineStore('phases', {
    state: () => ({
        phases: [],
    }),
    actions: {
        async fetchPhases() {
            try {
                const response = await axios.get('http://127.0.0.1:8000/phase-planner/phase/');
                this.phases = response.data;
                console.log(this.phases)
            } catch (error) {
                console.error('Error fetching phases:', error);
            }
        },
    },
});
