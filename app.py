import os
import flask
import flask_socketio
from os.path import join, dirname
from dotenv import load_dotenv
import flask_sqlalchemy
import models

MESSAGES_RECEIVED_CHANNEL_KEY = "all messages"


app = flask.Flask(__name__)

socketio = flask_socketio.SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

dotenv_path = join(dirname(__file__), 'sql.env')
load_dotenv(dotenv_path)

sql_user = os.environ['SQL_USER']
sql_pwd = os.environ['SQL_PASSWORD']

database_uri = 'postgresql://{}:{}@localhost/db'.format(sql_user, sql_pwd)

app.config['SQLALCHEMY_DATABASE_URI'] = database_uri

db = flask_sqlalchemy.SQLAlchemy(app)
db.app = app

db.create_all()
db.session.commit()


messages_list = []


def emit_all_messages(channel):
    # we are going to emit to 'all messages'
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

@socketio.on('new message')
def on_new_message(data):
    print("Got an event for new message input with data:", data)
    
    db.session.add(models.Messages(data["message"]));
    db.session.commit();
    
    emit_all_messages(MESSAGES_RECEIVED_CHANNEL_KEY)


@app.route('/')
def hello():
    emit_all_messages(MESSAGES_RECEIVED_CHANNEL_KEY)
    return flask.render_template('index.html')
    
# @socketio.on('new message')
# def on_new_message(data):
#     print("Got an event for new message with data:", data)
#     message_text = data['message']
#     if message_text in messages_list:
#         print(message_text + " is already in the list!")
#     else:
#         print("Added " + message_text + " to the list! Your list is now : ")
#         messages_list.append(message_text)
#         print(messages_list)
#     socketio.emit('message received', {
#         'message': message_text
#     })

if __name__ == '__main__': 
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )