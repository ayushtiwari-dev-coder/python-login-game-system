# 🎮 Python Login Game System

A modular command-line game platform built in **Python**.

Started as a simple CLI project → evolved into a structured system with:

- Authentication system
- Session management
- SQL database storage
- AI-driven gameplay

---

# 🚀 How to Run

```bash
cd login_system
python main.py
```

⚠️ Only run **main.py**  
Do **NOT** run internal files directly.

---

# 📁 Project Structure

```
login_system/
├── main.py
├── login_logic.py
├── security.py
├── session_manager.py
├── database/
│   ├── connection.py
│   └── sqlhandler.py
├── rock_paper_scissor/
│   └── main.py
├── hand_cricket/
│   ├── main.py
│   ├── game_logic.py
│   └── ai_brain_logic.py
└── data/
```

---

# 🔐 Authentication System

Features:

- Account creation with validation
- Username rules
- Password strength checking
- Password hashing (SHA256)
- Login attempt limit
- **3 wrong attempts → 5 minute lockout**
- Auto-login via saved session

---

# 🧠 Session Manager

- Detects saved session on launch
- Automatically logs user in
- Logout clears session
- Prevents unauthorized access

---

# 💾 Database System

User data is now stored using **MySQL** instead of JSON.

Features:

- SQL tables for users and game stats
- Persistent player statistics
- Secure database connection using environment variables
- `.env` file for protecting database credentials

---

# ✊ Rock Paper Scissors

### Modes

**Endless Mode**

- unlimited rounds
- exit anytime

**Limited Mode**

- fixed rounds (max 20)

**Ranked Mode**

- fixed 10 rounds
- no early exit (anti-cheat)

### Stats

- Wins
- Losses
- Draws
- Win Rate

---

# 🏏 Hand Cricket

### Core Rules

Both players choose numbers **1–6**

- Same number → **OUT**
- Otherwise → runs scored

### Match Flow

1. Toss (Odd/Even)
2. First Innings → set target
3. Second Innings → chase target
4. Tie → **Super Over**

### Features

- Live scoreboard
- Target tracking
- Commentary system
- Reaction timer
- Match summary
- Persistent stats

---

# ⏱ Reaction Timer System

Players must respond within **3 seconds**.

If player is slow:

- **Batting → -20 runs**
- **Bowling → +20 runs to computer**

👉 Creates pressure and forces decision patterns.

---

# 🔥 Super Over System

- Each side plays **6 balls**
- Highest score wins
- Tie → repeat

👉 No draws possible.

---

# 🤖 AI Brain System

The AI is **not random**.  
It uses a **4-layer decision system**.

---

## 🧩 Layer 1 — Motive Engine

Determines strategy based on match situation.

### Batting

- Calculates required run rate
- Adjusts aggression dynamically

### Bowling

- Reads player pressure
- Adjusts targeting

---

## 🎯 Strategies

- **Freestyle** → low pressure → random bias
- **Balanced** → medium pressure → middle numbers
- **Aggressive** → high pressure → 4,5,6
- **Conservative** → safe → low numbers
- **Desperate** → extreme → heavy 5,6
- **Bowling High** → player under pressure
- **Bowling Normal** → balanced
- **Bowling Low** → easy target

---

## 📊 Layer 2 — Frequency Tracking

Tracks player history.

Detects the **most used number**.

Behavior:

- Bowling → target it
- Batting → avoid it

---

## 🔁 Layer 3 — Recency Tracking

Tracks last **5 moves**.

Numbers not used recently get **higher probability**.

---

## ⚙️ Layer 4 — Weighted Decision

Final Decision =

```
Motive + Frequency + Recency
```

- Motive → base weights
- Frequency → strong signal (+10)
- Recency → fine tuning (+2)

---

# 🧠 AI Result

- Early game → simple AI
- Late game → adaptive AI

👉 AI becomes harder over time.

---

# 📈 Player Statistics

Tracks:

- Matches played
- Wins
- Losses
- Win rate

Stored in the **database for persistence**.

---

# 🚧 Future Plans

- Difficulty modes
- Persistent AI memory
- Leaderboard system
- Advanced statistics
- More games

---

# 👨‍💻 Author

**Ayush Tiwari**

GitHub:  
https://github.com/ayushtiwari-dev-coder

---

# 📜 License

MIT License