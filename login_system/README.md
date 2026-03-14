# Terminal Login Game System 🎮

A modular Python terminal application that combines a **login system, session management, mini-games, and player statistics tracking**.

This project demonstrates how to build a **backend-style system architecture in Python** using modules, file handling, and structured program flow.

---

# Features

## 🔐 Authentication System
- Create account
- Login system
- Password hashing
- Protection against repeated wrong password attempts

---

## 👤 Session System
- Automatically logs the user in if a session exists
- Logout clears the saved session
- Persistent session stored locally

---

## 🎮 Game System

### Rock Paper Scissors
Includes two modes:

**Endless Mode**
- Play unlimited rounds
- Stop anytime to finish the match

**Limited Mode**
- Play a fixed number of rounds
- Winner determined after all rounds

Game results automatically update player statistics.

---

## 📊 Profile Stats Dashboard
Displays player statistics including:

- Total Matches Played
- Wins
- Losses
- Draws
- Win Rate (%)

---

## 🧩 Modular Architecture

The project is structured using multiple modules to separate responsibilities.

Each module handles a specific responsibility:

| Module | Purpose |
|------|------|
| main.py | Application entry point |
| login_logic.py | Account creation and login validation |
| file_handler.py | User data storage |
| session_manager.py | Session persistence |
| rock_paper_scissor | Game engine |

---

# How to Run the Program

⚠️ Important:

Run the program **from the `login_system` folder**, not from `python_projects`.

---

## Step 1 — Navigate to the project folder

---

## Step 2 — Run the application

---

# Data Storage

User data and session information are stored locally inside the `data` folder.

These files store:

- User credentials
- Player statistics
- Active session information

The `data` folder is ignored in Git to prevent uploading personal data.

---

# Future Improvements

Planned features include:

- Hand Cricket game
- Leaderboard system
- Additional statistics
- More mini-games
- Improved UI formatting

---

# Technologies Used

- Python
- JSON file storage
- Modular programming
- Terminal-based interface

---

# License

MIT License