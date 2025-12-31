from flask import request, redirect, session, url_for
from flask_mail import Message
from db import get_db

def contact_routes(app, mail):

    # ---------- ADD CONTACT ----------
    @app.route("/contact", methods=["POST"])
    def contact():
        form = request.form

        db = get_db()
        cur = db.cursor()
        cur.execute(
            """
            INSERT INTO contacts
            (name, phone, email, category, date, message)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                form["name"],
                form["phone"],
                form["email"],
                form["category"],
                form["date"],
                form["message"]
            )
        )
        db.commit()
        db.close()

        msg = Message(
            subject=f"New enquiry from {form['name']}",
            sender=app.config["MAIL_USERNAME"],
            recipients=[app.config["MAIL_USERNAME"]],
            body=form["message"]
        )
        mail.send(msg)

        return redirect("/")

    # ---------- DELETE CONTACT ----------
    @app.route("/delete_contact/<int:contact_id>", methods=["POST"])
    def delete_contact(contact_id):
        if not session.get("admin"):
            return redirect("/admin")

        db = get_db()
        cur = db.cursor()
        cur.execute(
            "DELETE FROM contacts WHERE id = ?",
            (contact_id,)
        )
        db.commit()
        db.close()


        return redirect(url_for("dashboard", section="contacts"))

