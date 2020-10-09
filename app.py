import os
import flask
import flask_socketio

app = flask.Flask(__name__)

socketio = flask_socketio.SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

messages_list = []

@app.route('/')
def hello():
    return flask.render_template('index.html')
    
@socketio.on('new message')
def on_new_message(data):
    print("Got an event for new message with data:", data)
    message_text = data['message']
    if message_text in messages_list:
        print(message_text + " is already in the list!")
    else:
        print("Added " + message_text + " to the list! Your list is now : ")
        messages_list.append(message_text)
        print(messages_list)
    socketio.emit('message received', {
        'message': message_text
    })

if __name__ == '__main__': 
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )