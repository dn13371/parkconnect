from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define your models here
class User(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    mail = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    activated = db.Column(db.Boolean, default=False) # 0 = not ative, 1 = active
    role = db.Column(db.Integer)

# Additional models can be added here
