from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/add_row', methods=['POST'])
def add_row():
    # Get all the languages from the form data
    languages = request.form.getlist('language')
    
    # Count the number of languages
    language_count = len(languages)
    
    # Debugging: print the list of languages and their count
    print("Languages:", languages)
    print("Number of languages:", language_count)
    
    # Return a response indicating the number of languages
    html = "<div class='flex flex-row'>"
    html += "<input type='text' name='text' class='w-64 border p-2'>"
    for language in languages:
        html += f"<div class='w-64 border p-2'>translate({language})</div>"
    html += "</div>"
    return html
    #return jsonify({'message': f'{language_count} languages received'})

if __name__ == '__main__':
    app.run(debug=True)
