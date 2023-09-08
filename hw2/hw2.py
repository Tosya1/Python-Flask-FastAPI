from flask import Flask, make_response, redirect, render_template, request, url_for

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    name = request.cookies.get('username')
    if request.method == 'POST':
        response = make_response(redirect(url_for('form')))
        response.delete_cookie('username')
        response.delete_cookie('email')
        return response
    context = {'title': 'Главная', 'name': name}
    return render_template('index.html', **context)


@app.route('/form/', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form['email']
        response = make_response(redirect(url_for('index')))
        response.set_cookie('username', username)
        response.set_cookie('email', email)
        return response
    return render_template('form.html', title='Авторизация')


if __name__ == '__main__':
    app.run(debug=True)
