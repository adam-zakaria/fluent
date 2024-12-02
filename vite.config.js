import { defineConfig } from 'vite'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [],
  server: {
    port: process.env.PORT || 5173, // Default to 5173 if PORT is not set
    host: '0.0.0.0',
  },
})
