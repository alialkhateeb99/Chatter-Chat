import os
import flask
import flask_socketio
from os.path import join, dirname
from dotenv import load_dotenv
import flask_sqlalchemy
import models
import json
from botfunctions import *

MESSAGES_RECEIVED_CHANNEL_KEY = "all messages"

app = flask.Flask(__name__)

socketio = flask_socketio.SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

dotenv_path = join(dirname(__file__), 'sql.env')
load_dotenv(dotenv_path)

database_uri = os.getenv('DATABASE_URL')

app.config['SQLALCHEMY_DATABASE_URI'] = database_uri

db = flask_sqlalchemy.SQLAlchemy(app)
db.init_app(app)
db.app = app

db.create_all()
db.session.commit()

def emit_all_messages(channel):
    all_messages = [ \
        db_message.message for db_message in \
        db.session.query(models.Messages).all() ]
        
    socketio.emit(channel,{
        'allMessages': all_messages
    })
    
@socketio.on('connect')
def on_connect():
    print('Someone connected!')
    socketio.emit('connected', {
        'test': 'Connected'
    })
    
    emit_all_messages(MESSAGES_RECEIVED_CHANNEL_KEY)

@socketio.on('disconnect')
def on_disconnect():
    print ('Someone disconnected!')
    socketio.emit('disconnect', {
        'test': 'Disconnected'
    })

@socketio.on('new message')
def on_new_message(data):
    print("Got an event for new message input with data:", data)
    
    db.session.add(models.Messages(data["message"]));
    result = get_bot_info(data["message"])
    if result != -1:
        db.session.add(models.Messages("ALIS_CHAT_BOT : " + result ))
        
    db.session.commit();
    emit_all_messages(MESSAGES_RECEIVED_CHANNEL_KEY)


@app.route('/')
def hello():
    emit_all_messages(MESSAGES_RECEIVED_CHANNEL_KEY)
    return flask.render_template('index.html')

if __name__ == '__main__': 
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )