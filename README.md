# Run
Local:
```
npm run dev
```
AWS:
```
npm run build
```

Flask:
```
python3 -m flask run --host=0.0.0.0 --port=3000 --debug
```

## Export api key
Update this path.
```
Export GOOGLE_APPLICATION_CREDENTIALS="/Users/azakaria/Code/polyglot_old/backend/helical-glass-264223-7cb954d1e0b4.json"
```

# TODO
* emptying an onchange does not empty the translation.
* Add delete row



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

