from flask import Flask, render_template
from db import get_db
from mail_config import init_mail

from admin import admin_routes
from project import project_routes
from contact import contact_routes
from feedback import feedback_routes

app = Flask(__name__)
app.secret_key = "admin_secret_key"

mail = init_mail(app)   

# Register routes
admin_routes(app)
project_routes(app)
contact_routes(app, mail)
feedback_routes(app)

@app.route("/")
def home():
    db = get_db()
    cur = db.cursor()
    feedbacks = cur.execute(
        "SELECT * FROM feedback WHERE approved=1"
    ).fetchall()
    videos = cur.execute("SELECT * FROM videos").fetchall()
    db.close()
    return render_template("index.html", feedbacks=feedbacks, videos=videos)

if __name__ == "__main__":
    app.run(debug=True)
