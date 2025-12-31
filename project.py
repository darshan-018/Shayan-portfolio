from flask import request, redirect, session, flash, url_for
from db import get_db
from helpers import extract_youtube_id

def project_routes(app):

    @app.route("/add-video", methods=["POST"])
    def add_video():
        if not session.get("admin"):
            return redirect("/admin")

        youtube_id = extract_youtube_id(request.form["youtube_input"])
        if not youtube_id:
            flash("Invalid YouTube link", "error")
            return redirect("/dashboard")

        db = get_db()
        cur = db.cursor()
        cur.execute(
            """
            INSERT INTO videos (category, title, youtube_id, description)
            VALUES (?, ?, ?, ?)
            """,
            (
                request.form["category"],
                request.form["title"],
                youtube_id,
                request.form["description"]
            )
        )
        db.commit()
        db.close()

        return redirect("/dashboard")

    @app.route("/delete-video/<int:id>")
    def delete_video(id):
        if not session.get("admin"):
            return redirect("/admin")

        db = get_db()
        cur = db.cursor()
        cur.execute("DELETE FROM videos WHERE id=?", (id,))
        db.commit()
        db.close()

        return redirect(url_for("dashboard", section="videos"))

