# Creating and Deploying a Multiplayer Wordle Game 

## Introduction 
This is a remake and upgrade of my WITS School Lab Project in Software development III Course
I build a famous wordle game that can be played online and involves multiple steps. 

### Technologies used
- Python to build backend 
- Utilizing Flask for the web server, 
- Socket.IO for real-time interactions, and 
- Basic HTML, JavaScript, CSS, and BootStrap for the front end.
- We also be using Azure to deploy game application 

````

Multiplayer with real-time synchronization using WebSockets.
A shared Wordle game where all players guess the same word.

````
---

### 1. Set Up the Project in VSCode

### Create a New Project Folder
- Open VSCode and create a new folder (wordle-multiplayer).
- Open a terminal in VSCode (Ctrl + ~ or View → Terminal).
- Create a Virtual Environment (Optional but Recommended)

Run the following command in the terminal:

```bash
    python -m venv venv
```
Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- Mac/Linux:
```bash
source venv/bin/activate
```

### 2. Install Required Python Packages
Run the following command in the terminal:
```bash
pip install flask flask-socketio eventlet
```
This installs:
- Flask → Web framework.
- Flask-SocketIO → Enables real-time multiplayer communication.
- eventlet → Required for WebSockets.

### 3. To run th