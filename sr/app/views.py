import json
from flask import flash, make_response, redirect, render_template, request, session, url_for
from app import app, os_info, current_time, users, db
from app.forms import ChangePasswordForm, FeedbackForm, LoginForm, TodoForm
from app.models import Feedback, Todo
from data import skills

@app.route('/')
def index():
    user_agent = request.user_agent
    return render_template('index.html', os_info=os_info, user_agent=user_agent, current_time=current_time)

@app.route('/about')
def about():
     return render_template('about.html')


@app.route('/skill')
@app.route('/skill/<int:idx>')
def skill(idx=None):
    if idx is not None:
        return render_template("skill.html",
                               idx=idx,
                               skills = skills)
    else:
        return render_template("skills.html",
                               skills = skills)


@app.route('/info')
def info():
    if 'name' not in session:
        flash('Hey there! Looks like you forgot to log in. Mind doing that first?', 'danger')
        return redirect(url_for('login'))
    name = session.get('name')
    cookies = request.cookies.items()
    form = ChangePasswordForm()
    return render_template(
        'info.html',
        name=name,
        cookies=cookies,
        form=form)


@app.route('/logout', methods=['POST'])
def logout():
    session.pop('name', None)
    flash('See you later, alligator! Successfully logged out.', 'info')
    return redirect(url_for('login'))


@app.route('/add_cookie', methods=['POST'])
def add_cookie():
    key = request.form.get('key')
    value = request.form.get('value')
    expiry = int(request.form.get('expiry'))
    flash(f'Successfully added a cookie with key "{key}"!', 'primary')
    resp = make_response(redirect(url_for('info')))
    resp.set_cookie(key, value, max_age=expiry)
    return resp


@app.route('/delete_cookie', methods=['POST'])
def delete_cookie():
    delete_key = request.form.get('delete_key')
    flash(f'Successfully deleted the cookie with key "{delete_key}"!', 'primary')
    resp = make_response(redirect(url_for('info')))
    resp.delete_cookie(delete_key)
    return resp


@app.route('/delete_all_cookies', methods=['POST'])
def delete_all_cookies():
    flash('All cookies successfully devoured!', 'primary')
    resp = make_response(redirect(url_for('info')))
    cookies = request.cookies
    for key in cookies.keys():
        resp.delete_cookie(key)
    return resp


@app.route("/login", methods=['GET', 'POST'])
def login():
    if 'name' in session:
        return redirect(url_for('info'))

    form = LoginForm()

    if form.validate_on_submit():
        name = form.username.data
        password = form.password.data
        remember = form.remember.data

        if name in users and users[name] == password:
            if remember:
                session['name'] = name
                flash('You have been logged in successfully to Info Page!', 'success')
                return redirect(url_for('info'))
            else:
                flash('You have been logged in successfully to Home Page!', 'success')
                return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'warning')
            return render_template("login.html", form=form)

    return render_template("login.html", form=form)

@app.route('/todo', methods=['GET', 'POST'])
def todo():
    form = TodoForm()
    todo_list = Todo.query.all()
    return render_template("todo.html", form=form, todo_list=todo_list)

@app.route('/add', methods=["POST"])
def add():
    form = TodoForm()

    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        new_todo = Todo(title=title, description=description, complete=False)
        db.session.add(new_todo)
        db.session.commit()
        flash('Todo added successfully', 'success')
    else:
        flash('Invalid input. Please try again.', 'danger')

    return redirect(url_for("todo"))

@app.route('/update/<int:todo_id>')
def update(todo_id):
    todo = db.get_or_404(Todo, todo_id)
    todo.complete = not todo.complete
    db.session.commit()
    flash('Todo updated successfully', 'success')
    return redirect(url_for('todo'))

@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    todo = db.get_or_404(Todo, todo_id)
    db.session.delete(todo)
    db.session.commit()
    flash('Todo deleted successfully', 'success')
    return redirect(url_for('todo'))

@app.route('/review', methods=['GET', 'POST'])
def review():
    form = FeedbackForm()

    if form.validate_on_submit():
        name = form.name.data
        text = form.text.data
        rating = form.rating.data
        feedback = Feedback(name=name, text=text, rating=rating)

        try:
            db.session.add(feedback)
            db.session.commit()
            flash('Your review has been added', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'An error occurred: {str(e)}', 'danger')

        return redirect(url_for("submit_review"))

    reviews = Feedback.query.all()
    return render_template("review.html", form=form, reviews=reviews)
