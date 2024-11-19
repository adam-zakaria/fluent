from flask import Flask, request, jsonify
from flask_cors import CORS
from google.cloud import translate_v2 as translate
from google.cloud import texttospeech

app = Flask(__name__)
CORS(app)

# Initialize translate and text to speech clients
translate_client = translate.Client()
tts_client = texttospeech.TextToSpeechClient()

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.json
    text = data.get('text')
    target_language = data.get('target_language')

    if not text or not target_language:
        return jsonify({'error': 'Text and target language are required'}), 400

    # Validate target_language
    valid_languages = ['en', 'es', 'fr', 'de', 'it', 'ja', 'zh']
    if target_language not in valid_languages:
        return jsonify({'error': f'Invalid target language: {target_language}'}), 400

    try:
        result = translate_client.translate(text, target_language=target_language)
        return jsonify({
            'translated_text': result['translatedText'],
            'source_language': result['detectedSourceLanguage']
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    data = request.json
    text = data['text']
    language_code = data['language_code']

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
        file_path = os.path.join('/tmp', filename)

        # Save the audio content to a file
        with open(file_path, 'wb') as out:
            out.write(response.audio_content)

        # Send the file
        return send_file(file_path, mimetype='audio/mpeg', as_attachment=True, download_name=filename)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
