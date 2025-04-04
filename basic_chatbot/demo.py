from flask import Flask, request, jsonify

app = Flask(__name__)

responses = {
    "hello": "Hi there! How can I help you?",
    "goodbye": "Goodbye! Have a great day!",
    "default": "I'm not sure how to respond to that."
}

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '').lower()
    reply = responses.get(user_input, responses['default'])
    return jsonify({'response': reply})

if __name__ == '__main__':
    app.run()
