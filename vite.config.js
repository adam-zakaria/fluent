import { defineConfig } from 'vite'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [],
  server: {
    port: 5173, // Default to 3000 if PORT is not set
    //port: 80, // Default to 3000 if PORT is not set
    host: '0.0.0.0',
  },
})
