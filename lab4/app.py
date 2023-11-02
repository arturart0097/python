from flask import Flask, request, render_template, redirect, url_for, session, flash, make_response
import json
import datetime

app = Flask("__name__")
app.secret_key = 'a1r1t1'

def authenticate(username, password):
    with open('users.json', 'r') as users_file:
        users = json.load(users_file)
        if username in users and users[username] == password:
            return True
    return False

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if authenticate(username, password):
            session['username'] = username
            flash('Успішний вхід!', 'success')
            return redirect(url_for('info'))
        else:
            flash('Невірне ім\'я користувача або пароль', 'danger')

    return render_template('login.html')

@app.route('/info', methods=['GET', 'POST'])
def info():
    if 'username' in session:
        username = session['username']

        cookies = request.cookies

        if request.method == 'POST':
            action = request.form.get('action')

            if action == 'add_cookie':
                key = request.form.get('key')
                value = request.form.get('value')
                expires = request.form.get('expires')

                if key and value:
                    expiration_time = datetime.datetime.now() + datetime.timedelta(seconds=int(expires))
                    response = make_response(redirect(url_for('info')))
                    response.set_cookie(key, value, max_age=expiration_time.timestamp())
                    flash(f'Кукі "{key}" успішно додано', 'success')
                    return response
                else:
                    flash('Необхідно ввести ключ та значення', 'danger')

            elif action == 'delete_cookie':
                key = request.form.get('key_to_delete')

                if key in cookies:
                    response = make_response(redirect(url_for('info')))
                    response.delete_cookie(key)
                    flash(f'Кукі "{key}" успішно видалено', 'success')
                    return response
                else:
                    flash('Кукі за вказаним ключем не знайдено', 'danger')

            elif action == 'delete_all_cookies':
                response = make_response(redirect(url_for('info')))
                for key in cookies.keys():
                    response.delete_cookie(key)
                flash('Усі кукі були успішно видалені', 'success')
                return response

        return render_template('info.html', username=username, cookies=cookies)

    return redirect(url_for('login'))

@app.route('/add_cookie', methods=['POST'])
def add_cookie():
    if 'username' in session:
        key = request.form.get('cookie_key')
        value = request.form.get('cookie_value')
        expires = int(request.form.get('cookie_expiration'))

        if key and value:
            expiration_time = datetime.datetime.now() + datetime.timedelta(seconds=expires)
            response = make_response(redirect(url_for('info')))
            response.set_cookie(key, value, expires=expiration_time)
            flash(f'Кукі "{key}" успішно додано', 'success')
            return response
        else:
            flash('Необхідно ввести ключ та значення', 'danger')
    return redirect(url_for('login'))


@app.route('/clear_cookies', methods=['POST'])
def clear_cookies():
    if 'username' in session:
        response = make_response(redirect(url_for('info')))
        for key in request.cookies.keys():
            response.delete_cookie(key)
        flash('Усі кукі були успішно видалені', 'success')
        return response
    return redirect(url_for('login'))


@app.route('/logout', methods=['POST'])
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
