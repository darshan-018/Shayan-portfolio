from flask import render_template, request, redirect, session, flash, url_for
from db import get_db

def admin_routes(app):

    @app.route("/admin", methods=["GET", "POST"])
    def admin_login():
        if request.method == "POST":
            db = get_db()
            cur = db.cursor()
            cur.execute(
                "SELECT * FROM admin WHERE username=? AND password=?",
                (request.form["username"], request.form["password"])
            )
            admin = cur.fetchone()
            db.close()

            if admin:
                session["admin"] = True
                return redirect("/dashboard")

            flash("Invalid credentials", "error")

        return render_template("admin_login.html")

    @app.route("/dashboard")
    def dashboard():
        if not session.get("admin"):
            return redirect("/admin")

        db = get_db()
        cur = db.cursor()

        # Fetch all necessary data
        videos = cur.execute("SELECT * FROM videos").fetchall()
        contacts = cur.execute("SELECT * FROM contacts").fetchall()
        pending_feedbacks = cur.execute("SELECT * FROM feedback WHERE approved=0").fetchall()
        approved_feedbacks = cur.execute("SELECT * FROM feedback WHERE approved=1").fetchall()
        todos = cur.execute("SELECT id, task, created_at FROM todo ORDER BY created_at DESC").fetchall()

        db.close()

        return render_template(
            "admin_dashboard.html",
            videos=videos,
            contacts=contacts,
            pending_feedbacks=pending_feedbacks,
            approved_feedbacks=approved_feedbacks,
            todos=todos
        )

    @app.route("/logout")
    def logout():
        session.clear()
        return redirect("/admin")

    # ------------------- TODO ROUTES -------------------
    @app.route("/add_todo", methods=["POST"])
    def add_todo():
        if not session.get("admin"):
            return redirect("/admin")
        task = request.form.get("task")
        if task:
            db = get_db()
            cur = db.cursor()
            cur.execute("INSERT INTO todo (task) VALUES (?)", (task,))
            db.commit()
            db.close()
            flash("Task added successfully", "success")
        return redirect(url_for("dashboard"))

    @app.route("/delete_todo/<int:id>", methods=["POST"])
    def delete_todo(id):
        if not session.get("admin"):
            return redirect("/admin")
        db = get_db()
        cur = db.cursor()
        cur.execute("DELETE FROM todo WHERE id=?", (id,))
        db.commit()
        db.close()
        flash("Task deleted successfully", "success")
        return redirect(url_for("dashboard"))
