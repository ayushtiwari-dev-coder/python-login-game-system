Terminal Login Game System 🎮
A modular Python terminal application that combines a login system, session management, mini-games, and player statistics tracking.
This project demonstrates how to build a backend-style system architecture in Python using modules, file handling, and structured program flow.
How to Run
⚠️ Important — Read Before Running
This project must be run from the login_system folder, not from python_projects or any parent folder.
Step 1 — Navigate to the correct folder:
cd login_system
Step 2 — Run the entry point:
python main.py
Do not run any other file directly. main.py is the only entry point for the entire application. Running login_logic.py, file_handler.py, or any game file directly will not work as expected.
Project Structure
login_system/
├── main.py                  ← Run this file only
├── login_logic.py
├── file_handler.py
├── session_manager.py
├── rock_paper_scissor/
│   └── main.py
├── hand_cricket/
│   └── main.py
└── data/                    ← Auto-generated, ignored by Git
Features
🔐 Authentication System
Create account with username and password validation
Login system with password hashing
Protection against repeated wrong password attempts (5 minute lockout after 3 failed attempts)
👤 Session System
Automatically logs the user in if a session exists
Logout clears the saved session
Persistent session stored locally — no need to login every time
🎮 Game System
Rock Paper Scissors
Two modes available:
Endless Mode — Play unlimited rounds, stop anytime to finish the match
Limited Mode — Play a fixed number of rounds, winner determined after all rounds
Hand Cricket
Full match engine with:
Odd/Even toss system with player choice
Two full innings — bat or bowl first
Endless Mode — Play until wicket falls
Limited Mode — Choose overs (1-10), over limit ends innings
Live scoreboard with runs and balls tracking
Target chase system in second innings
Match summary with toss result and full scorecard
Game results automatically update player statistics.
📊 Profile Stats Dashboard
Displays player statistics including:
Total Matches Played
Wins / Losses / Draws
Win Rate (%)
🧩 Modular Architecture
Each module handles a specific responsibility:
Module
Purpose
main.py
Application entry point
login_logic.py
Account creation and login validation
file_handler.py
User data storage and retrieval
session_manager.py
Session persistence and auto-login
rock_paper_scissor/
RPS game engine
hand_cricket/
Hand Cricket game engine
Data Storage
User data and session information are stored locally inside the data folder.
These files store:
User credentials
Player statistics
Active session information
The data folder is ignored in Git to prevent uploading personal data.
Future Improvements
Planned features include:
Frequency based AI opponent for Hand Cricket
Leaderboard system
Additional player statistics (strike rate, average, win streaks)
More mini-games
Improved UI formatting
Technologies Used
Python
JSON file storage
Modular programming
Terminal-based interface
License
MIT License