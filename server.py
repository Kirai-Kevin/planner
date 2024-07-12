from flask import Flask, request, jsonify, send_from_directory
from adaptive_learning import customize_content
from gemini_utils import generate_content
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/generate_plan', methods=['POST'])
def generate_plan():
    user_type = request.form['user-type']
    subject = request.form['subject']
    language = request.form['language']
    topic = request.form['topic']
    form = request.form['form']

    if user_type == 'teacher':
        duration = request.form['lesson-duration']
        additional_info = request.form['learning-objectives']
        plan_type = "lesson"
    else:
        duration = request.form['revision-duration']
        additional_info = request.form['difficulty']
        plan_type = "revision"

    content_request = customize_content(plan_type, subject, topic, form, duration, additional_info, language)
    generated_content = generate_content(content_request, subject, topic, form, user_type, language)

    return jsonify({"plan": generated_content})

if __name__ == '__main__':
    app.run(debug=False)