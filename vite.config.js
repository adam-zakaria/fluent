import { defineConfig } from 'vite'

// https://vitejs.dev/config/
export default defineConfig(({ mode }) => {
  return {
    plugins: [],
    server: {
       watch: {
         ignored: ['**/node_modules/**', '**/venv/**']
       },
      port: process.env.PORT || 5173, // Default to 5173 if PORT is not set
      host: '0.0.0.0',
      hmr: mode === 'aws_dev', // Enable HMR only in 'aws_dev' mode
    },
  };
});
