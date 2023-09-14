#Создать форму для регистрации пользователей на сайте. Форма должна содержать поля "Имя", "Фамилия", "Email", "Пароль" и кнопку #"Зарегистрироваться". При отправке формы данные должны сохраняться в базе данных, а пароль должен быть зашифрован.

from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash
from registration import Registration
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SECRET_KEY'] = '99b4019e592dca7c32e15725b60006e6755fd289880562e6abdf49cbc90d892f'
csrf = CSRFProtect(app)
db.init_app(app)

@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')

@app.route('/<name>')
def hello_name(name):
    return render_template('index.html', name=name)

@app.route('/reg/', methods=['GET', 'POST'])
def reg():
    form = Registration()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        password = generate_password_hash(form.password.data)
        new_user = User(name = name, last_name = form.last_name.data, email = form.email.data, password = password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('hello_name', name=name))
    return render_template('registration.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)