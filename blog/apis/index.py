# index 接口文件
from flask import session, escape, url_for
from flask import request, render_template, flash, redirect, Blueprint
import time

from blog.service.user_service import UserService

index_bp = Blueprint("index_bp", __name__)


@index_bp.route('/user_register', methods=['GET', 'POST'])  # 注册
def longin_judge():
    if request.method == 'POST':
        data = request.form

        UserService().register(data)
        return render_template('auth/login.html')
    return render_template('auth/register_file.html')


@index_bp.route('/', methods=['GET', 'POST'])  # 登陆
def user_login():
    if request.method == "GET":
        return render_template('auth/login.html')
    else:
        uname = request.form['username']
        password = request.form['pwd']
        u1 = User.query.filter_by(username=uname).one()
        # print('u1',u1)
        user_logining = u1.nickname
        print(user_logining)
        session['auto'] = user_logining
        user = User.query.all()
        # print(user)
        for i in user:
            ID = i.id
            session['num'] = ID
            dpwd = i.password
            md5 = hashlib.md5()
            md5.update(userpwd.encode('utf8'))
            md5_pwd = md5.hexdigest()
            print(md5_pwd)
            if uname == i.username and dpwd == md5_pwd:
                # print(user)
                # print(type(user))
                # print(user.username)
                return redirect(url_for('showfiles', user_logining=user_logining))
            else:
                return render_template('auth/login.html')


@index_bp.route('/success', methods=['GET', 'POST'])  # homesite  添加文件信息
def content():
    form = MyFrom()
    if request.method == 'GET':
        return render_template('add_page.html', form=form)
    else:
        if form.validate_on_submit():
            usernick = escape(session['auto'])
            print('usernick---------------------->>', usernick)
            userid = escape(session['num'])  # session   用户表的id
            print('userid------------------------->>', userid)
            # blogs = escape(session['blogs'])
            # print('blogs------------------------->>>',blogs)
            res = time.strftime('%Y-%m-%d %H:%M:%S %A')
            cont = form.AllFile.data
            filename = form.fname.data.filename
            title = form.title.data
            file_info = Blog_content(usernick, filename, cont, title, userid)
            db.session.add(file_info)
            db.session.commit()
            form.fname.data.save('Imgs/{}'.format(filename))
            return redirect(url_for('showfiles', user_login=user_login, res=res))
        return render_template('add_page.html', form=form)


@index_bp.errorhandler(404)
def not_find(e):
    return '没找到界面'


@index_bp.route('/showallfiles', methods=['GET', 'POST'])  # 查看
def showfiles():
    res = time.strftime('%Y-%m-%d %H:%M:%S %A')
    blogs = Blog_content.query.all()
    print(blogs)
    for i in blogs:
        id = i.id
        print('id------------------------------------------------------>>>>>>>>>>>>>>>>>>>>>>', id)
    # session['blogs'] = blogs
    print(blogs)
    return render_template('blog_page.html', blogs=blogs, res=res)


@index_bp.route('/showblos/<int:blog_id>', methods=['GET', 'POST'])
def showblog(blog_id):
    blog = Blog_content.query.filter_by(id=blog_id).one()
    return render_template('showblog.html', blog=blog)


@index_bp.route('/update_blog/<int:blogid>', methods=['GET', 'POST'])
def update(blogid):
    return ''
