from flask import Flask, render_template, request
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app, cors_allowed_origins='*')

@socketio.on('message')
def handleMessage(msg):
	print('Message: ' + msg)
	send(msg, broadcast=True)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		name = request.form.get('name')
		return render_template('index.html', name=name)

	return render_template('register.html')


if __name__ == '__main__':
	app.run(debug=True)