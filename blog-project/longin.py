from flask import render_template,Blueprint

#创建蓝图对象
bp = Blueprint('blog',__name__)

@bp.route('/')
def blog_login():
    return  render_template('login.html')


@bp.route('/register')
def blog_register():
    return render_template('register_file.html')


@bp.route('/success')
def login_success():
    return render_template('blog_home.html')


