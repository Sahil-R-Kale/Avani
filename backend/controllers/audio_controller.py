import time
from flask import request, make_response, jsonify,send_file
from codescripts.main import get_farmer_data 
from utilities.general_utils import add_univariate_text,add_bivariate_text

def send_response(data, code):
    '''
    The function generates JSON response according to given result 
    Args:
    data: data to be returned
    code: HTTP message code
    Returns: 
    result: JSON response
    '''
    response = make_response(
        jsonify(
            data
        ),
        code,
    )
    response.headers["Content-Type"] = "application/json"
    return response

def audio_controller():
    data = {}
    try:
        farmer_name = request.form['farmer_name']
        timestamps = eval(request.form['timestamps'])
        audio = request.files['audio']
        audio.save(f'inputs/{farmer_name}.wav')
        data.update({
            'farmer':farmer_name,
            'time':timestamps
        })
        # process_audio(audio) //Link to your AI Model functions
        return send_response({
                    'data':data,
                    'message': 'Audio processed succesfully. Farmer response has been processed and added to the database',
                    'code': 200,
                    'success': True
                }, 200)

        
    except:
        message = "Cannot process given input"
        code = 404
        success = False
        return send_response({
                    'message': message,
                    'code': code,
                    'success': success
                }, 200)

def display_controller():
    data = {}
    try:
        farmer_name = request.form['farmer_name']
        data = get_farmer_data(farmer_name)

        return send_response({
                    'data':data,
                    'code': 200,
                    'success': True
                }, 200)
    except:
        message = "Cannot process given input"
        code = 404
        success = False
        return send_response({
                    'message': message,
                    'code': code,
                    'success': success
                }, 200)

def insight_controller():
    data = []
    try:
        if request.form['button_pressed'] == 'Textual Insights':
            if 'analysis_type' in request.form:
                    analysis_types = request.form.getlist('analysis_type')
                    if 'Univariate Analysis' in analysis_types:
                            data = add_univariate_text(data)
                    if 'Bivariate Analysis' in analysis_types:
                            data = add_bivariate_text(data)
            return send_response({
                    'data':data,
                    'code': 200,
                    'success': True
                }, 200)
        elif request.form['button_pressed'] == 'Graphical Insights':
            if 'analysis_type' in request.form:
                    analysis_types = request.form.getlist('analysis_type')
                    if 'Univariate Analysis' in analysis_types:
                            return send_file('utilities/Univariate_Graphs.png')
                    elif 'Bivariate Analysis' in analysis_types:
                            return send_file('utilities/Bivariate_Graphs.png')
        return send_response({
                    'code': 200,
                    'success': True
                }, 200)
    except:
        message = "Cannot process given input"
        code = 404
        success = False
        return send_response({
                    'message': message,
                    'code': code,
                    'success': success
                }, 200)