# Run
## Local
`npm run dev`
Loads .env and .env.development

## AWS
see deploy_all.sh

## Notes
`npm run dev:aws_dev` calls from `package.json``"dev:aws_dev": "vite --mode aws_dev"`. `vite.config.js` does things based on mode, i.e. set hot reload for dev but not prod `hmr: mode === 'aws_dev', // Enable HMR only in 'aws_dev' mode`


# Hosting
We used route53, gandi and nginx. We took the route53 nameservers and added it to the gandi dashboard (I think). We added a policy to the IAM user 'adam' (route53_fluent), to allow some route53 CRUD. Generated certs with certbot and added it to flask. Redirected 80 to 5173 in nginx.

# Certs
List certs:
`sudo certbot certificates`

Nginx is configured to forward http to https, and it is working.

Nginx and the .env's needed to be updated for the backend to be https. Look at /etc/nginx/nginx.conf and .env for more.

## Export api key
Update this path.
`Export GOOGLE_APPLICATION_CREDENTIALS="/Users/azakaria/Code/polyglot_old/backend/helical-glass-264223-7cb954d1e0b4.json"`

# If the translation randomly stops working, confirm GOOGLE_APPLICATION_CREDENTIALS is set to the correct key.
export GOOGLE_APPLICATION_CREDENTIALS="/home/ubuntu/Code/fluent/key.json"