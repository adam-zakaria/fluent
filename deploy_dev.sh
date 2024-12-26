# frontend at 5174
# backend at 3001
pm2 start 'npm run aws_dev' --name fluent_vite_dev && pm2 start 'python3 -m flask run --host=0.0.0.0 --port=3001 --debug' --name fluent_flask_dev