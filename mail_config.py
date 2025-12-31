from flask_mail import Mail

def init_mail(app):
    app.config.update(
        MAIL_SERVER="smtp.gmail.com",
        MAIL_PORT=587,
        MAIL_USE_TLS=True,
        MAIL_USERNAME="shayancsenq@gmail.com",
        MAIL_PASSWORD="oeou jyki smcm ehim"
    )
    return Mail(app)
