from app import app 

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.sqlite'  # (2.)

db = SQLAlchemy()  # (3.)
db.init_app(app)

class User(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    mail = db.Column(db.String, primary_key=False)
    username = db.Column(db.String, primary_key=False)
    password = db.Column(db.Integer, primary_key=False)
    activated = db.Column(db.Boolean, primary_key=False, default = False)
    role = db.Column(db.Integer, primary_key=False) 