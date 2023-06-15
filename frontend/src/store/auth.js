// Import the necessary dependencies
import { defineStore } from 'pinia';

// Import axios for API requests
import axios from 'axios';

// Define the Pinia store
export const useAuthStore = defineStore('auth', {
    state: () => ({
        token: null, // Holds the authentication token
        user: null,  // Holds the user information
    }),

    actions: {
        // Method to log in and get the authentication token
        async login(username, password) {
            try {
                const response = await axios.post('/accounts/token/login/', {
                    username,
                    password,
                });
                this.token = response.data.auth_token;
                return true;
            } catch (error) {
                console.error('Login error:', error);
                return false;
            }
        },

        // Method to log out and clear the authentication token
        async logout() {
            try {
                await axios.post('/accounts/token/login/');
                this.token = null;
                this.user = null;
            } catch (error) {
                console.error('Logout error:', error);
            }
        },


    },
});
