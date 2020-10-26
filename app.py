"""
#app.py
Backend server logic for react-flask application
"""

import os
from os.path import join, dirname
import flask
import flask_socketio
from dotenv import load_dotenv
import flask_sqlalchemy
import botfunctions


MESSAGES_RECEIVED_CHANNEL_KEY = "all messages"
SOCKET_CONNECT_KEY = "connect"
SOCKET_ON_CONNECT_KEY = "connected"
SOCKET_DISCONNECT_KEY = "disconnect"
ON_NEW_MESSAGE_KEY = "new message"
KEY_IS_BOT_COMMAND = "is_bot"
KEY_BOT_COMMAND = "bot_command"
KEY_BOT_RESULT = "bot_result"

app = flask.Flask(__name__)

socketio = flask_socketio.SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

dotenv_path = join(dirname(__file__), "sql.env")
load_dotenv(dotenv_path)

database_uri = os.getenv("DATABASE_URL")

app.config["SQLALCHEMY_DATABASE_URI"] = database_uri

db = flask_sqlalchemy.SQLAlchemy(app)
import models

db.init_app(app)
db.app = app

db.create_all()
db.session.commit()


def emit_all_messages(channel):
    '''
    This function emits all messages from DB to client
    '''
    all_messages = [
        db_message.message for db_message in db.session.query(models.Messages).all()
    ]

    socketio.emit(channel, {"allMessages": all_messages})


@socketio.on(SOCKET_CONNECT_KEY)
def on_connect():
    '''
    When a new user is connected, this function
    emits all messages from DB to client each time
    '''
    socketio.emit(SOCKET_ON_CONNECT_KEY, {"test": "Connected"})

    emit_all_messages(MESSAGES_RECEIVED_CHANNEL_KEY)


@socketio.on(SOCKET_DISCONNECT_KEY)
def on_disconnect():
    '''
    When a new user is disconnected, this
    function emits that a user has disconnected
    '''
    socketio.emit("disconnect", {"test": "Disconnected"})


@socketio.on(ON_NEW_MESSAGE_KEY)
def on_new_message(data):
    '''
    When a new message is received this function
    checks wether it is an image/botfunction
    then adds it to the database.
    '''
    db.session.add(models.Messages(data["message"]))
    bot_result = botfunctions.get_bot_info(data["message"])
    if bot_result[KEY_BOT_RESULT] != -1 and bot_result[KEY_IS_BOT_COMMAND]:
        db.session.add(models.Messages("ALIS_CHAT_BOT : " + bot_result[KEY_BOT_RESULT]))
    image_result = botfunctions.check_message_image(data["message"])
    if image_result != -1:
        db.session.add(models.Messages(image_result))

    db.session.commit()
    emit_all_messages(MESSAGES_RECEIVED_CHANNEL_KEY)


@app.route("/")
def hello():
    '''
    Starting point for application
    returns static index.html file
    '''
    emit_all_messages(MESSAGES_RECEIVED_CHANNEL_KEY)
    return flask.render_template("index.html")


if __name__ == "__main__":
    socketio.run(
        app,
        host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", 8080)),
        debug=True,
    )
