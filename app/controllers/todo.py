import time
from flask import render_template, flash, redirect, g
from flask.ext.login import login_required
from app import app, db
from app.models import Todo
from app.forms import TodoForm

@app.route('/todos', methods = ['GET', 'POST'])
@login_required
def todos():
    todos = g.user.todos.all()
    form = TodoForm()
    if form.validate_on_submit():
        todo = Todo(user_id = g.user.get_id(), body = form.body.data)
        db.session.add(todo)
        db.session.commit()
        return redirect('/todos')
    return render_template('todos/index.html',
        todos = todos,
        form = form)