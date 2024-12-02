# Run
Local:
```
npm run dev
```
Loads .env and .env.development

On AWS we're running a dev and prod build: frontend and backend. prod front is 5173 with VITE_API_HOST=https://fluent.monster/api and dev front is 5174 with VITE_API_HOST=https://dev.fluent.monster/api

To run a build specify it in the package.json like 

"scripts": {
  "dev": "vite",
  "build": "vite build",
  "preview": "vite preview",
  "dev:aws": "PORT=5174 vite --mode aws"
},

npm run dev:aws will load .env.aws and run the dev server on port 5174. It seems like PORT didn't actually work but since 5173 is taken by prod it just tried 5174 so that's fine.

and the config in 
export default defineConfig({
  plugins: [],
  server: {
    port: process.env.PORT || 5173, // Default to 5173 if PORT is not set
    host: '0.0.0.0',
  },
})

Okay so using dev.fluent.monster requires DNS changes and cert changes and that's all kind of unnecessary at this point. Maybe we can just use an IP. 

i.e. 

VITE_API_HOST=http://54.167.31.12:3001/api
I think we can just bypass the nginx and go straight to the vite server.

## Dev
pm2 start 'python3 -m flask run --host=0.0.0.0 --port=3001 --debug' --name fluent_flask_dev
pm2 start 'npm run dev:aws' --name fluent_dev


```
npm run build
```

Flask:
prod
```
python3 -m flask run --host=0.0.0.0 --port=3000 --debug
```
dev
```
python3 -m flask run --host=0.0.0.0 --port=3001 --debug
```

# Hosting
We used route53, gandi and nginx. We took the route53 nameservers and added it to the gandi dashboard (I think). We added a policy to the IAM user 'adam' (route53_fluent), to allow some route53 CRUD. Generated certs with certbot and added it to flask. Redirected 80 to 5173 in nginx.

# Certs
List certs:
```
sudo certbot certificates
```
Nginx is configured to forward http to https, and it is working.

Nginx and the .env's needed to be updated for the backend to be https. Look at /etc/nginx/nginx.conf and .env for more.

## Export api key
Update this path.
```
Export GOOGLE_APPLICATION_CREDENTIALS="/Users/azakaria/Code/polyglot_old/backend/helical-glass-264223-7cb954d1e0b4.json"
```
# TODO
* collapse borders
* use textarea for translation cell
* it seems like the textarea innerhtml is getting set to the translationcellcontents...actually because it's a textarea this is probably how it works.























---------------------------------

# Translate API key
Translate api will automatically look for key in path specified here.

# HTMX talking points
* form data centric
* HATEOAS
  * state stored in html (not 'double state' in frontend, (js + html))
* single file
* felt like writing simple apps in react was way more a pain that I wanted it to be (FOR ME)
* tailwind not working with server markup

# style prefs
* single file
* lierate programming
* html as state
* one dev shop
* minimize cognitive load
  * clojure
  * ruby consistency
* globals (refactor when the time comes: let's deal with scale, in the very unlikely event scale ever comes)

