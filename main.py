from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

messages = []

@app.route('/')
def index():
    return render_template('chat.html', messages=messages)

@app.route('/send', methods=['POST'])
def send():
    username = request.form['username']
    message = request.form['message']
    messages.append({'username': username, 'message': message})
    return jsonify({'username': username, 'message': message})

if __name__ == '__main__':
    app.run()



