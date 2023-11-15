from flask import render_template, Blueprint
from blog.schema.from_schema import MyFrom

# 创建蓝图对象
auto_bp = Blueprint('auto_bp', __name__)


#
@auto_bp.route('/')
def blog_login():
    return render_template('auth/login.html')


@auto_bp.route('/register')
def blog_register():
    return render_template('auth/register_file.html')


@auto_bp.route('/success')
def login_success():
    form = MyFrom()
    return render_template('add_page.html', form=form)


@auto_bp.route('/about')
def about():
    return render_template('about.html')
