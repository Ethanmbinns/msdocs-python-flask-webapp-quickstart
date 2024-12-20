from flask import Flask
from flask_socketio import SocketIO

# Initialize Flask app
app = Flask(__name__)
# Initialize SocketIO with the Flask app
socketio = SocketIO(app)

# WebSocket event handler for user connection
@socketio.on('connect')
def handle_connect():
    print('User connected')
    # Emit a welcome message to the client
    socketio.emit('message', 'Hello')

# Run the app
if __name__ == '__main__':
    # Run the SocketIO server
    socketio.run(app, debug=True)
