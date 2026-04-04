from flask import Flask, flash, redirect, render_template, request, session
from cs50 import SQL
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///users.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


def login_required(f):

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function


@app.route("/login", methods=["GET", "POST"])
def login():

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("em"):
            return render_template('wrong.html')

        # Ensure password was submitted
        elif not request.form.get("pw"):
            return render_template('wrong.html')

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("em")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("pw")
        ):
            return render_template('wrong.html')

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        username = request.form.get("un")
        password = request.form.get("pw")
        confirmation = request.form.get("confirmation")
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("un")
        )
        session["username"] = username
        if not username:
            return render_template('wrong.html')
        if not password:
            return render_template('wrong.html')
        if password != confirmation:
            return render_template('wrong.html')
        if len(rows) != 0:
            return render_template('wrong.html')

        hashed = generate_password_hash(password)
        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, hashed)

        userid = db.execute("SELECT id FROM users WHERE username = ?", username)[0]["id"]
        session["user_id"] = userid
        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/")
@login_required
def index():
    nameR = db.execute("SELECT username FROM users WHERE id = ?", session['user_id'])
    name = nameR[0]['username']
    return render_template("csgame.html", name=name)


@app.route("/hex1", methods=['POST', 'GET'])
@login_required
def hex():
    if request.method == 'POST':
        streak = request.form.get('streak')
        score = request.form.get('score')
        game = request.form.get('game')

        if not score or not streak or not game:
            return render_template("wrong.html")

        # Convert score and streak to integers
        score = int(score)
        streak = int(streak)

        # Check if user already has a score for this game
        existing = db.execute(
            "SELECT score FROM scores WHERE user_id = ? AND game = ?", session['user_id'], game)

        if existing:
            # Update only if the new score is higher
            if score > existing[0]['score']:
                db.execute("UPDATE scores SET score = ?, streak = ? WHERE user_id = ? AND game = ?",
                           score, streak, session['user_id'], game)
        else:
            # Insert new record if none exists
            db.execute("INSERT INTO scores (user_id, score, streak, game) VALUES (?, ?, ?, ?)",
                       session['user_id'], score, streak, game)

        return 'ok', 200

    else:
        return render_template("hex1.html")


@app.route("/hex2", methods=['POST', 'GET'])
@login_required
def hex2():
    if request.method == 'POST':
        streak = request.form.get('streak')
        score = request.form.get('score')
        game = request.form.get('game')

        if not score or not streak or not game:
            return render_template("wrong.html")

        score = int(score)
        streak = int(streak)

        existing = db.execute(
            "SELECT score FROM scores WHERE user_id = ? AND game = ?", session['user_id'], game)

        if existing:
            if score > existing[0]['score']:
                db.execute("UPDATE scores SET score = ?, streak = ? WHERE user_id = ? AND game = ?",
                           score, streak, session['user_id'], game)
        else:
            db.execute("INSERT INTO scores (user_id, score, streak, game) VALUES (?, ?, ?, ?)",
                       session['user_id'], score, streak, game)

        return 'ok', 200

    else:
        return render_template("hex2.html")


@app.route("/binary", methods=['POST', 'GET'])
@login_required
def bin():
    if request.method == 'POST':
        streak = request.form.get('streak')
        score = request.form.get('score')
        game = request.form.get('game')

        if not score or not streak or not game:
            return render_template("wrong.html")

        # Convert score and streak to integers
        score = int(score)
        streak = int(streak)

        # Check if user already has a score for this game
        existing = db.execute(
            "SELECT score FROM scores WHERE user_id = ? AND game = ?", session['user_id'], game)

        if existing:
            # Update only if the new score is higher
            if score > existing[0]['score']:
                db.execute("UPDATE scores SET score = ?, streak = ? WHERE user_id = ? AND game = ?",
                           score, streak, session['user_id'], game)
        else:
            # Insert new record if none exists
            db.execute("INSERT INTO scores (user_id, score, streak, game) VALUES (?, ?, ?, ?)",
                       session['user_id'], score, streak, game)

        return 'ok', 200

    else:
        return render_template("binary.html")


@app.route("/binary2", methods=['POST', 'GET'])
@login_required
def bin2():
    if request.method == 'POST':
        streak = request.form.get('streak')
        score = request.form.get('score')
        game = request.form.get('game')

        if not score or not streak or not game:
            return render_template("wrong.html")

        # Convert score and streak to integers
        score = int(score)
        streak = int(streak)

        # Check if user already has a score for this game
        existing = db.execute(
            "SELECT score FROM scores WHERE user_id = ? AND game = ?", session['user_id'], game)

        if existing:
            # Update only if the new score is higher
            if score > existing[0]['score']:
                db.execute("UPDATE scores SET score = ?, streak = ? WHERE user_id = ? AND game = ?",
                           score, streak, session['user_id'], game)
        else:
            # Insert new record if none exists
            db.execute("INSERT INTO scores (user_id, score, streak, game) VALUES (?, ?, ?, ?)",
                       session['user_id'], score, streak, game)

        return 'ok', 200

    else:
        return render_template("binary2.html")


@app.route("/leader")
@login_required
def leader():

    players = db.execute("SELECT COUNT(*) AS total FROM users")
    users = players[0]['total']

    games_played = db.execute("SELECT COUNT(*) AS games FROM scores")
    games = games_played[0]['games']

    highest_score = db.execute("SELECT score FROM scores ORDER BY score DESC LIMIT 1")
    score = highest_score[0]['score']

    scores = db.execute("""
        SELECT u.username, s.score, s.streak, s.game
        FROM scores s
        JOIN users u ON s.user_id = u.id
        ORDER BY s.score DESC
        LIMIT 50
    """)
    nameR = db.execute("SELECT username FROM users WHERE id = ?", session['user_id'])
    name = nameR[0]['username']
    return render_template("leader.html", scores=scores, users=users, games=games, score=score, name=name)


if __name__ == "__main__":
    app.run()

