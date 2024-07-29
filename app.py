from flask import Flask, render_template, request
from db import db  , User
import click
from faker import Faker

app = Flask(__name__)

# Load configuration from a separate file or from app.py itself
app.config.from_mapping(
    SECRET_KEY='secret_key_just_for_dev_environment',
    SQLALCHEMY_DATABASE_URI='sqlite:///todos.sqlite',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

# Initialize SQLAlchemy with the Flask application
db.init_app(app)

# Ensure CLI command is registered correctly
@app.cli.command('init-db')
def init_db():
    db.create_all()
    # Generate mock data and populate database
    fake = Faker()
    for _ in range(10):  # Create 10 users (adjust as needed)
        user = User(
            mail=fake.email(),
            username=fake.user_name(),
            password="password",  # Replace with your password hashing logic
            activated=True,
            role=1  # Adjust role value based on your needs
        )
        db.session.add(user)
    db.session.commit()
    click.echo('Database initialized and mock data populated.')
# Routes and other application logic here
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        dbpass = db.session.query(User.password).filter(User.mail == email).scalar()
        if dbpass:   
            if dbpass == password: 
                return "login success"
        else: 
            return "email not registered"
        

    if request.method == 'GET':
        return render_template('base.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        results = db.session.query(User).filter(User.mail == email).all()
        if results :
            return "mail already exists"
        else:
            user = User(
                mail = email,
                username= "default",
                password= password, 
                activated=False,
                role=1  
                )
            db.session.add(user) 
            db.session.commit()

            return "user added successfully"
        
    if request.method == 'GET':
        return render_template('register.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
