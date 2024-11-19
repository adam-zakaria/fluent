from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

langs = ["english", "spanish", "mandarin", "japanese", "russian", "hindi", "arabic", "portuguese"]
lang_index=2 # start with 2 because 0 and 1 are reserved for english and spanish, which are default starters in the table
num_rows=2

@app.route('/add_col', methods=['POST'])
def add_col():
    # Create a select element with the current language at lang_index
    html = f'<div><select hx-swap-oob="beforeend:.flex-row0" name="language" class="w-64 language border p-2">'
    html += f'<option value="{langs[lang_index]}">{langs[lang_index]}</option>'
    html += '</select></div>'
    
    # Append a div with the current language for each row
    for row in range(1, num_rows):
        html += f'<div hx-swap-oob="beforeend:.flex-row{row}">{langs[lang_index]}</div>'
    
    return html
  

@app.route('/add_row', methods=['POST'])
def add_row():
    global num_rows
    num_rows+=1
    # Get all the languages from the form data
    languages = request.form.getlist('language')
    html = "<div class='overflow-x-auto'>"
    html += "<input type='text' name='text' class='w-64 border p-2'></input>"
    # skip english
    for i in range(0, len(languages)-1):
        html += f"<div class='w-64 border p-2 inline-block'>{languages[i+1]}</div>"
    html += "</div>"
    return html

if __name__ == '__main__':
    app.run(debug=True)
