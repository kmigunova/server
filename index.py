from flask import Flask, session, redirect, render_template, request
from models import UsersModel, AccessoriesModel
from db import DB


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db = DB()
UsersModel(db.get_connection()).init_table()
AccessoriesModel(db.get_connection()).init_table()


@app.route('/')
@app.route('/index')
def index():
    return render_template('table.html', title='Просмотр')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if 'username' not in session:
        if request.method == 'GET':
            return render_template('login.html', title='Вход')
    return redirect('/order')


@app.route('/logout')
def logout():
    session.pop('username', 0)
    return redirect('/login')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('form.html', title='Регистрация')
    return redirect('/order')


@app.route('/order', methods=['POST', 'GET'])
def order():
    if request.method == 'GET':
        return render_template('order.html', title='Заказываем товар')
    return redirect('/success')


@app.route('/success')
def success():
    return render_template('success.html', title='Успешно')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
