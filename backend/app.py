from flask import Flask
from routes.audio_bp import audio_bp
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

app.register_blueprint(audio_bp)

@app.route('/')
def hello():
    return 'Flask app running successfully'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)