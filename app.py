from flask import Flask, render_template, request, jsonify
import json
import tensorflow as tf
from chatbot import predict_class, get_response

app = Flask(__name__)

# Load chatbot data and model
intents = json.loads(open('intents.json').read()) # Load intents as you did in chatbot.py
model = tf.keras.models.load_model('chatbot_model.h5')# Load model as you did in chatbot.py

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    intents_list = predict_class(user_message, model)
    response = get_response(intents_list, intents)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
