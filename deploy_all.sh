# These lines in package.json explain a lot
# "aws_dev": "PORT=5174 vite --mode aws_dev",
# "aws_prod": "vite build && serve -s dist -l 5173"
# --mode aws_dev loads .env.aws_dev
# There is no --mode for 'vite build', it assumes --mode production, which uses .env.production

# dev
pm2 start 'npm run aws_dev' --name fluent_vite_dev && pm2 start 'python3 -m flask run --host=0.0.0.0 --port=3001 --debug' --name fluent_flask_dev

# Prod
pm2 start 'npm run aws_prod' --name fluent_vite_prod && pm2 start 'python3 -m flask run --host=0.0.0.0 --port=3000 --debug' --name fluent_flask_prod