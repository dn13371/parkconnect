from flask import Flask, render_template, request
import db
import os
import jinja2
app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY='secret_key_just_for_dev_environment',
    DATABASE=os.path.join(app.instance_path, 'todos.sqlite')
)
app.cli.add_command(db.init_db)
app.cli.add_command(db.insert_mock)
app.teardown_appcontext(db.close_db_con)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        return f'Email: {email}, Password: {password}'
        
    if request.method == 'GET':
        return render_template('base.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        return f'Email: {email}, Password: {password}'
        
    if request.method == 'GET':
        return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
