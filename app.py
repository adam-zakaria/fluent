from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from google.cloud import translate_v2 as translate
from google.cloud import texttospeech
import os

import uuid

app = Flask(__name__)
CORS(app)

# Initialize translate and text to speech clients
translate_client = translate.Client()
tts_client = texttospeech.TextToSpeechClient()

@app.route('/api/translate', methods=['POST'])
def translate_text():
    print('/api/translate')
    data = request.json
    text = data.get('phrase')
    target_language = data.get('target_language')

    if not text or not target_language:
        print(text, target_language)
        return jsonify({'error': 'Text and target language are required'}), 400

    language_map = {
        'english': 'en',
        'spanish': 'es',
        'mandarin': 'zh',
        'japanese': 'ja',
        'russian': 'ru',
        'hindi': 'hi',
        'arabic': 'ar',
        'portuguese (br)': 'pt-BR',
        'french': 'fr',
        'bengali': 'bn',
        'urdu': 'ur',
        'indonesian': 'id',
        'german': 'de',
        'thai': 'th'
    }

    if target_language not in language_map:
        return jsonify({'error': f'Invalid target language: {target_language}'}), 400

    try:
        result = translate_client.translate(text, target_language=language_map[target_language])
        return jsonify({
            'translated_text': result['translatedText'],
            'source_language': result['detectedSourceLanguage']
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/text-to-speech', methods=['POST'])
def text_to_speech():
    print('/api/text-to-speech', flush=True)
    language_map = {
        'english': 'en-US',
        'spanish': 'es-ES',
        'mandarin': 'cmn-CN',
        'japanese': 'ja-JP',
        'russian': 'ru-RU',
        'hindi': 'hi-IN',
        'arabic': 'ar-XA',
        'portuguese (br)': 'pt-BR',
        'french': 'fr-FR',
        'bengali': 'bn-BD',
        'urdu': 'ur-PK',
        'indonesian': 'id-ID',
        'german': 'de-DE',
        'thai': 'th-TH'
    }

    data = request.json
    text = data['text']
    language_code = language_map[data['language']]

    try:
        synthesis_input = texttospeech.SynthesisInput(text=text)

        voice = texttospeech.VoiceSelectionParams(
            language_code=language_code,
            ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
        )

        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )

        response = tts_client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )

        # Generate a unique filename
        filename = f"speech_{uuid.uuid4()}.mp3"
        file_path = os.path.join('./', filename)

        # Save the audio content to a file
        with open(file_path, 'wb') as out:
            out.write(response.audio_content)

        # Send the file
        return send_file(file_path, mimetype='audio/mpeg', as_attachment=True, download_name=filename)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
