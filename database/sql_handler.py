from database.connection import get_connection


# Create all tables (run once at start)
def create_tables():
    db = get_connection()
    cursor = db.cursor()

    users_table = """
    CREATE TABLE IF NOT EXISTS users (
        username VARCHAR(50) PRIMARY KEY,
        name VARCHAR(50),
        password VARCHAR(255),
        lock_until BIGINT
    )
    """

    rps_table = """
    CREATE TABLE IF NOT EXISTS rps_stats (
        username VARCHAR(50),
        wins INT,
        losses INT,
        matches INT,
        draws INT,
        FOREIGN KEY (username) REFERENCES users(username)
    )
    """

    hand_table = """
    CREATE TABLE IF NOT EXISTS hand_cricket_stats (
        username VARCHAR(50),
        wins INT,
        losses INT,
        matches INT,
        highest_score INT,
        FOREIGN KEY (username) REFERENCES users(username)
    )
    """

    cursor.execute(users_table)
    cursor.execute(rps_table)
    cursor.execute(hand_table)

    db.commit()
    cursor.close()
    db.close()


# Create a new user
def create_user(username, name, password):
    db = get_connection()
    cursor = db.cursor()

    user_query = """
    INSERT INTO users (username, name, password, lock_until)
    VALUES (%s, %s, %s, %s)
    """

    rps_query = """
    INSERT INTO rps_stats (username, wins, losses, matches, draws)
    VALUES (%s, %s, %s, %s, %s)
    """

    hand_query = """
    INSERT INTO hand_cricket_stats (username, wins, losses, matches, highest_score)
    VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(user_query, (username, name, password, 0))
    cursor.execute(rps_query, (username, 0, 0, 0, 0))
    cursor.execute(hand_query, (username, 0, 0, 0, 0))

    db.commit()
    cursor.close()
    db.close()


def get_user(username):
    db = get_connection()
    cursor = db.cursor(dictionary=True)

    query = "SELECT * FROM users WHERE username = %s"
    cursor.execute(query, (username,))

    user = cursor.fetchone()

    cursor.close()
    db.close()

    return user


def update_rps_stats(username, result):
    db = get_connection()
    cursor = db.cursor()

    if result == "wins":
        query = """
        UPDATE rps_stats
        SET wins = wins + 1,
            matches = matches + 1
        WHERE username = %s
        """

    elif result == "losses":
        query = """
        UPDATE rps_stats
        SET losses = losses + 1,
            matches = matches + 1
        WHERE username = %s
        """

    elif result == "draws":
        query = """
        UPDATE rps_stats
        SET draws = draws + 1,
            matches = matches + 1
        WHERE username = %s
        """

    cursor.execute(query, (username,))
    db.commit()
    cursor.close()
    db.close()

def update_hand_cricket_stats(username, result):
    db = get_connection()
    cursor = db.cursor()

    if result == "wins":
        query = """
        UPDATE hand_cricket_stats
        SET wins = wins + 1,
            matches = matches + 1
        WHERE username = %s
        """

    elif result == "losses":
        query = """
        UPDATE hand_cricket_stats
        SET losses = losses + 1,
            matches = matches + 1
        WHERE username = %s
        """

    cursor.execute(query, (username,))
    db.commit()
    cursor.close()
    db.close()

def update_lock(username, lock_until):

    db = get_connection()
    cursor = db.cursor()

    query = """
    UPDATE users
    SET lock_until = %s
    WHERE username = %s
    """

    cursor.execute(query, (lock_until, username))

    db.commit()
    cursor.close()
    db.close()

def update_name(username, name):

    db = get_connection()
    cursor = db.cursor()

    query = """
    UPDATE users
    SET name = %s
    WHERE username = %s
    """

    cursor.execute(query, (name, username))

    db.commit()
    cursor.close()
    db.close()