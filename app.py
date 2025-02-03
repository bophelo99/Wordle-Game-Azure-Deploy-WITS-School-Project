"""
This file contains the server-side code for the multiplayer game. It uses Flask and 
Flask-SocketIO to handle the game logic and communication between clients. 
The game is a simple word guessing game where players try to guess a word based on 
feedback provided by the server. The server maintains the game state for each 
room and broadcasts updates to all players in the room.
"""

import random
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit, join_room #, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app, cors_allowed_origins="*")

# Global game state organized by rooms
rooms = {}

# Word list for the game
WORDS = ["apple", "grape", "peach", "melon", "berry"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    if not username:
        return jsonify({"success": False, "message": "Username is required!"}), 400
    return jsonify({"success": True, "username": username})

@socketio.on('create_room')
def create_room(data):
    room_name = data.get('room')
    if not room_name or room_name in rooms:
        emit('error', {'message': 'Invalid or existing room name!'})
        return

    rooms[room_name] = {"word": random.choice(WORDS), "guesses": []}
    join_room(room_name)
    emit('room_created', {'room': room_name})
    emit('update_game', rooms[room_name], room=room_name)

@socketio.on('join_room')
def join_room_handler(data):
    room_name = data.get('room')
    if room_name not in rooms:
        emit('error', {'message': 'Room does not exist!'})
        return

    join_room(room_name)
    emit('room_joined', {'room': room_name})
    emit('update_game', rooms[room_name], room=room_name)

@socketio.on('guess')
def handle_guess(data):
    room_name = data.get('room')
    guess = data.get('guess')

    if room_name not in rooms or len(guess) != len(rooms[room_name]['word']):
        emit('error', {'message': 'Invalid guess or room!'})
        return

    feedback = [
        'correct' if char == rooms[room_name]['word'][i] else
        'present' if char in rooms[room_name]['word'] else
        'absent' for i, char in enumerate(guess)
    ]

    rooms[room_name]['guesses'].append({"guess": guess, "feedback": feedback})
    emit('update_game', rooms[room_name], room=room_name)

@socketio.on('reset')
def reset_game(data):
    room_name = data.get('room')
    if room_name not in rooms:
        emit('error', {'message': 'Invalid room!'})
        return

    rooms[room_name] = {"word": random.choice(WORDS), "guesses": []}
    emit('update_game', rooms[room_name], room=room_name)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
