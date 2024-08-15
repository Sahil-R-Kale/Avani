from flask import Blueprint
from controllers.audio_controller import audio_controller,display_controller,insight_controller

audio_bp = Blueprint('audio_bp', __name__)

audio_bp.route('/process_audio', methods=['POST'])(audio_controller)
audio_bp.route('/show_data', methods=['POST'])(display_controller)
audio_bp.route('/get_insights', methods=['POST'])(insight_controller)

