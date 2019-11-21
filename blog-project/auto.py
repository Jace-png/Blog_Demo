from flask import render_template, Blueprint
from flask import Flask,redirect
import dbs
# 创建蓝图对象
bp = Blueprint('blog', __name__)


#
@bp.route('/')
def blog_login():
    return render_template('auth/login.html')


@bp.route('/register')
def blog_register():
    return render_template('auth/register_file.html')

@bp.route('/success')
def login_success():
    form = dbs.MyFrom()
    return render_template('add_page.html',form = form)

@bp.route('/about')
def about():
    return render_template('about.html')