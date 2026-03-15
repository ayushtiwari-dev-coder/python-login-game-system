# Python Login Game System

A modular command-line game platform written in Python that includes a full login system, session management, persistent player statistics, and multiple games.

The project started as a simple CLI project and gradually evolved into a structured game system with AI-driven gameplay and persistent user data.

---

## Features

- Login & User Authentication System
- Persistent User Data Storage
- Session Management
- Multiple CLI Games
- AI-Driven Hand Cricket Opponent
- Player Statistics Tracking
- Dynamic Commentary System
- Reaction Timer with Penalty System
- Super Over System for Tie Matches

---

## Project Architecture

The project is divided into multiple modules to keep the system modular and scalable.

project/

login_system/

authentication.py

session_manager.py

user_database.py

file_handler/

file_handler.py

games/

rock_paper_scissors.py

hand_cricket/

game_logic.py

ai_brainlogic.py

main.py

README.md

---

## Login System

The login system allows users to create accounts and securely access the game platform.

Features:

- User Registration
- User Login
- Session Handling
- Persistent Data Storage

User data is saved using the file handler module so that progress and statistics remain stored between sessions.

---

## Session Manager

The session manager tracks the currently logged-in user and manages the active session.

Responsibilities:

- Track logged-in users
- Handle login/logout flow
- Prevent unauthorized access to game systems

---

## File Handler

The file handler module is responsible for managing persistent storage.

Responsibilities:

- Save user data
- Load user profiles
- Update game statistics
- Maintain player records across sessions

---

## Games Included

### Rock Paper Scissors

Classic CLI implementation of Rock-Paper-Scissors with statistics tracking.

Features:

- Player vs Computer gameplay
- Win/Loss/Draw tracking
- Win rate calculation
- Persistent statistics

---

### Hand Cricket

A fully featured command-line version of hand cricket with an intelligent AI opponent.

Features:

- Toss System (Odd/Even)
- Batting and Bowling mechanics
- Endless Mode
- Limited Overs Mode
- AI-driven opponent behavior
- Match summary system
- Player statistics tracking

---

## AI Brain Logic

The AI opponent adapts its playstyle depending on match situations.

The AI calculates a **motive** based on:

- Current score
- Target
- Remaining balls
- Required run rate
- Match situation

Possible motives include:

- Freestyle
- Balanced
- Aggressive
- Conservative
- Desperate
- Bowling High Pressure
- Bowling Normal
- Bowling Defensive

Each motive uses **weighted probability** to select numbers, making the AI feel strategic rather than random.

---

## Dynamic Commentary System

The game includes a dynamic commentary engine to improve gameplay experience.

Different commentary is triggered based on events.

Commentary categories include:

- Random events
- Four runs
- Six runs
- Player out

Example commentary:

Both players hiding their fingers carefully...

Same fingers! OUT!

Massive SIX from the batter!

Commentary is randomly selected from predefined lists.

---

## Reaction Timer System

To simulate pressure, the player has **3 seconds** to enter a number during gameplay.

If the player exceeds the time limit:

Batting Penalty

-20 runs deducted

Bowling Penalty

Computer receives +20 runs

This adds reaction pressure and strategic gameplay.

---

## Super Over System

If both teams score the same runs, a Super Over is triggered.

Rules:

Each side gets **6 balls**.

The highest score wins.

If tied again, another Super Over begins.

---

## Match Summary

After every match the system prints:

- Toss result
- First innings score
- Second innings score
- Match winner

Statistics are then saved using the file handler system.

---

## Future Improvements

Possible future improvements include:

- Smarter adaptive AI
- Difficulty levels
- Leaderboards
- Multiplayer mode
- GUI interface
- More games

---

## Author

Ayush Tiwari

GitHub:  
https://github.com/ayushtiwari-dev-coder

---

## License

This project is open source and available under the MIT License.