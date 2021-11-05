from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from KanbanFlask.auth import login_required
from KanbanFlask.db import get_db

bp = Blueprint('board', __name__, url_prefix = "/board")

@bp.route('/main_board')
def main_board():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, task_status, assignee, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('board/main_board.html', posts=posts)

@bp.route('/user_board')
@login_required
def user_board():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, task_status, assignee, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('board/user_board.html', posts=posts)