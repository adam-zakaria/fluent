from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/add_row', methods=['POST'])
def add_row():
    # Get all the languages from the form data
    languages = request.form.getlist('language')
    html = "<div class='flex flex-row overflow-x-auto'>"
    html += "<input type='text' name='text' class='w-64 border p-2 flex-none'>"
    for language in languages:
        html += f"<div class='w-64 border p-2 flex-none'></div>"
    html += "</div>"
    return html
    #return jsonify({'message': f'{language_count} languages received'})

if __name__ == '__main__':
    app.run(debug=True)
