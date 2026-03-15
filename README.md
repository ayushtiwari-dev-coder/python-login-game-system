🎮 Python CLI Game System
A modular command-line game platform built in Python with a full login system, session management, persistent player statistics, and multiple games including Hand Cricket and Rock-Paper-Scissors.
This project focuses on clean architecture, modular game logic, AI behavior design, and persistent user data management.
📌 Features
🔐 Login & User Management System
💾 Persistent Player Data Storage
🧠 AI-driven Hand Cricket Opponent
🎮 Multiple Games
📊 Player Statistics Tracking
🔄 Session Management
🎤 Dynamic Commentary System
⏱ Reaction Timer with Penalty System
🔁 Super Over Logic for Tie Matches
🏗 Project Architecture
The project is structured into multiple modules, each responsible for a specific system.
Copy code

project/
│
├── login_system
│   ├── authentication
│   ├── session_manager
│   └── user_database
│
├── file_handler
│
├── games
│   ├── rock_paper_scissors
│   ├── hand_cricket
│   │   ├── game_logic
│   │   └── ai_brainlogic
│
└── main.py
Each system is separated to keep the code modular, maintainable, and scalable.
🔐 Login System
The login system manages user authentication and profile management.
Responsibilities
Register new users
Login existing users
Maintain active sessions
Store player statistics
Load player data on login
When a user logs in:
Copy code

User Input
   ↓
Authentication
   ↓
Session Creation
   ↓
Load Player Data
   ↓
Game Dashboard
User data is stored persistently using the file handler system.
🔄 Session Manager
The Session Manager keeps track of the currently logged-in player.
Responsibilities
Maintain active session
Prevent unauthorized access
Provide player identity to games
Load player stats automatically
Example session data:
Copy code

current_user
username
game_stats
session_state
The session manager ensures all games know which player is currently playing.
💾 File Handler System
The File Handler manages persistent storage of user data.
Responsibilities
Save player statistics
Load existing profiles
Update match results
Maintain game history
Stored player stats include:
Copy code

matches played
wins
losses
draws
highest score
This system ensures player progress is saved across sessions.
🎮 Available Games
The platform currently includes two games.
1️⃣ Rock-Paper-Scissors
Classic Rock-Paper-Scissors against the computer.
Features:
Computer opponent
Match result tracking
Player statistics update
Game flow:
Copy code

Player chooses move
Computer selects move
Winner determined
Stats updated
2️⃣ Hand Cricket
The primary game in this project.
A digital version of the popular hand cricket game played with numbers.
🏏 Hand Cricket Gameplay
Basic Rules
Players choose a number between 1 and 6.
If both numbers match → OUT
If numbers differ → runs are scored
Example:
Copy code

Player: 4
Computer: 2

Runs Scored = 4
Example Out:
Copy code

Player: 3
Computer: 3

OUT
🎲 Toss System
Before the match begins, a toss determines who bats first.
Steps:
Player chooses Odd or Even
Both select numbers
Sum determines winner
Copy code

Total = Player + Computer
Even → Even wins
Odd → Odd wins
Toss winner chooses:
Copy code

Bat
Bowl
🏏 Game Modes
Endless Mode
No over limit
Innings continues until the batter is out
Limited Mode
Player chooses 1–10 overs
Each over = 6 balls
The game automatically handles:
Copy code

ball tracking
target calculation
run rate pressure
🧠 AI Brain Logic
The Hand Cricket AI uses strategy-based decision making instead of pure randomness.
The AI evaluates the match situation before choosing numbers.
Factors considered
Copy code

current score
balls remaining
target score
required run rate
projected final score
From this information the AI selects a motive.
🎯 AI Motives
Examples of motives used by the AI:
Copy code

freestyle
balanced
aggressive
conservative
desperate
bowling_high
bowling_normal
bowling_low
Each motive has a different probability distribution for selecting numbers.
Example aggressive weights:
Copy code

[1,1,2,3,4,4]
Meaning:
Higher chance of 4, 5, 6
Lower chance of 1, 2
This allows the AI to simulate strategic batting and bowling behavior.
🎤 Dynamic Commentary System
The game includes a dynamic commentary engine to improve gameplay experience.
Different commentary is triggered based on events.
Commentary Categories
Copy code

Random events
Four runs
Six runs
Player out
Example commentary:
Copy code

"Both players hiding their fingers carefully..."
"Same fingers! OUT!"
"Massive SIX from the batter!"
Commentary is randomly selected from predefined lists.
⏱ Reaction Timer System
To simulate pressure, the player has 3 seconds to enter a number during gameplay.
If the player exceeds the time limit:
Batting Penalty
Copy code

-20 runs deducted
Bowling Penalty
Copy code

Computer receives +20 runs
This adds reaction pressure and strategic gameplay.
🔥 Super Over System
If both teams score the same runs:
Copy code

First Score = Second Score
A Super Over is triggered.
Rules:
Each side gets 6 balls
Highest score wins
If tied again → another super over
📊 Match Summary
After every match the system prints:
Copy code

Toss result
First innings score
Second innings score
Match winner
Statistics are then saved using the file handler system.
🧠 AI + Strategy Design
The AI was designed to simulate human-like strategic play.
Example behaviors:
Copy code

Accelerate when required run rate increases
Play safe when score projection is high
Bowl aggressively under pressure
This makes the computer opponent adaptive instead of random.
🛠 Technologies Used
Copy code

Python 3
Random module
Time module
File I/O
Custom AI logic
The entire project runs as a Command Line Interface (CLI) application.
🚀 Future Improvements
Potential upgrades planned:
Player pattern learning AI
Difficulty levels
Improved bowling strategy
GUI version
Online multiplayer
📌 Project Goals
This project focuses on practicing:
Copy code

system architecture
game engine logic
AI behavior design
state management
file handling
modular Python programming
🎯 Final Note
This project evolved from simple CLI experiments into a fully structured multi-game platform with AI-driven gameplay and persistent player data.
It demonstrates how a command-line program can be designed with clean architecture, modular systems, and intelligent game logic.