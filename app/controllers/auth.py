from flask import request, render_template, flash, redirect, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, lm, db
from app.forms import LoginForm, RegisterForm
from app.models import User

@app.before_request
def before_request():
    g.user = current_user

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect('/todos')
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user is None:
            flash('Invalid username')
            return redirect('/login')
        else:
            if (form.password.data != user.password):
                flash('Invalid password')
                return redirect('/login')
            login_user(user)
            flash('Login successfull')
            return redirect(request.args.get('next') or '/todos')
    return render_template('login.html',
        form = form)

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(name = form.name.data, username = form.username.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful')
        return redirect('/login')
    return render_template('register.html',
        form = form)