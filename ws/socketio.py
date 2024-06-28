from flask import Flask, render_template
from flask_socketio import SocketIO, send

def setup_socketio(app):
    socketio = SocketIO(app, path='/api/socket.io')

    @socketio.on('message')
    def handle_message(msg):
        print('Message: ' + msg)
        send(msg, broadcast=True)
