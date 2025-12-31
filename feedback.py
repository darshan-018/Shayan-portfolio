from flask import request, redirect, session, flash, url_for
from db import get_db

def feedback_routes(app):

    # ---------- SUBMIT FEEDBACK ----------
    @app.route("/submit_feedback", methods=["POST"])
    def submit_feedback():
        db = get_db()
        cur = db.cursor()
        cur.execute(
            """
            INSERT INTO feedback (name, rating, description, approved)
            VALUES (?, ?, ?, 0)
            """,
            (
                request.form["name"],
                int(request.form["rating"]),
                request.form["description"]
            )
        )
        db.commit()
        db.close()

        flash("Feedback submitted for approval", "success")
        return redirect(url_for("home"))

    # ---------- APPROVE FEEDBACK ----------
    @app.route("/approve_feedback/<int:feedback_id>")
    def approve_feedback(feedback_id):
        if not session.get("admin"):
            return redirect("/admin")

        db = get_db()
        cur = db.cursor()
        cur.execute(
            "UPDATE feedback SET approved = 1 WHERE id = ?",
            (feedback_id,)
        )
        db.commit()
        db.close()

        return redirect("/dashboard")

    # ---------- DELETE FEEDBACK ----------
    @app.route("/delete_feedback/<int:feedback_id>")
    def delete_feedback(feedback_id):
        if not session.get("admin"):
            return redirect("/admin")

        db = get_db()
        cur = db.cursor()
        cur.execute(
            "DELETE FROM feedback WHERE id = ?",
            (feedback_id,)
        )
        db.commit()
        db.close()

        return redirect(url_for("dashboard", section="feedback"))

