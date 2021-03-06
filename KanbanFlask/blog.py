# Blog blueprint, from blog itself to any of the posts modifications

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from KanbanFlask.auth import login_required
from KanbanFlask.db import get_db

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, task_status, assignee, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('blog/index.html', posts=posts)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        task_status = request.form['task_status']
        assignee = request.form['assignee']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, task_status, assignee, author_id)'
                ' VALUES (?, ?, ?, ?, ?)',
                (title, body, task_status, assignee, g.user['id'])
            )
            db.commit()
            return redirect(url_for('board.main_board'))

    return render_template('blog/create.html')

'''
Because the functionality of getting a posts information will probably occur
throughout the application, it makes sense to separate and abstract it into 
its own function
 '''
def get_post(id, check_author=True):
    post = get_db().execute(
        'SELECT p.id, title, body, task_status, assignee, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post

@bp.route('/<int:id>/view_post', methods=('GET',))
@login_required
def view_post(id):
    post = get_db().execute(
        'SELECT p.id, title, body, task_status, assignee, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    return render_template('blog/view_post.html', post=post)

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        task_status = request.form['task_status']
        assignee = request.form['assignee']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE post SET title = ?, body = ?, task_status = ?, assignee = ?'
                ' WHERE id = ?',
                (title, body, task_status, assignee, id)
            )
            db.commit()
            return redirect(url_for('board.main_board'))

    return render_template('blog/update.html', post=post)

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('board.main_board'))

