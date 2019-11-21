# index 接口文件
from flask import Flask, session, escape, url_for
from flask import request, render_template, flash, redirect
from dbs import MyFrom, db, User, app, Blog_content
import hashlib
import time


@app.route('/user_register', methods=['GET', 'POST'])  # 注册
def longin_judge():
    if request.method == 'POST':
        nickname = request.form['Nickname']
        username = request.form['Newusername']
        upwd = request.form['Newupwd']
        upwd2 = request.form['Newupwd2']
        print(username)
        print(type(username))
        if 10 <= len(username) <= 12 and 8 <= len(upwd) <= 15 and upwd == upwd2 and username != upwd and len(nickname)<=12:
            md5 = hashlib.md5()
            md5.update(upwd.encode('utf8'))
            md5_pwd = md5.hexdigest()
            print(md5_pwd)
            add_user = User(nickname = nickname, username = username,password=md5_pwd)
            # print(add_user)
            db.session.add(add_user)
            db.session.commit()
            return render_template('auth/login.html')
        else:
            flash('注册失败!请注意格式和长度')
            return render_template('auth/register_file.html')
    return render_template('auth/register_file.html')


@app.route('/', methods=['GET', 'POST'])  # 登陆
def user_login():
    # form = MyFrom()
    if request.method == "GET":
        return render_template('auth/login.html')
    else:
        uname = request.form['username']
        userpwd = request.form['pwd']
        u1 = User.query.filter_by(username=uname).one()
        # print('u1',u1)
        user_logining = u1.nickname
        print(user_logining)
        session['auto'] = user_logining
        user = User.query.all()
        # print(user)
        for i in user:
            ID= i.id
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
                return redirect(url_for('showfiles',user_logining=user_logining))
            else:
                return render_template('auth/login.html')


@app.route('/success', methods=['GET', 'POST'])  # homesite  添加文件信息
def content():
    form = MyFrom()
    if request.method == 'GET':
        return render_template('add_page.html', form=form)
    else:
        if form.validate_on_submit():
            usernick = escape(session['auto'])
            print('usernick---------------------->>',usernick)
            userid = escape(session['num'])  # session   用户表的id
            print('userid------------------------->>',userid)
            # blogs = escape(session['blogs'])
            # print('blogs------------------------->>>',blogs)
            res = time.strftime('%Y-%m-%d %H:%M:%S %A')
            cont = form.AllFile.data
            filename = form.fname.data.filename
            title = form.title.data
            file_info = Blog_content(usernick, filename,cont,title, userid)
            db.session.add(file_info)
            db.session.commit()
            form.fname.data.save('Imgs/{}'.format(filename))
            return redirect(url_for('showfiles',user_login = user_login,res = res))
        return render_template('add_page.html', form=form)
@app.errorhandler(404)
def not_find(e):
    return '没找到界面'


@app.route('/showallfiles', methods=['GET', 'POST'])   #查看
def showfiles():
    res = time.strftime('%Y-%m-%d %H:%M:%S %A')
    blogs = Blog_content.query.all()
    print(blogs)
    for i in blogs:
        id = i.id
        print('id------------------------------------------------------>>>>>>>>>>>>>>>>>>>>>>',id)
    # session['blogs'] = blogs
    print(blogs)
    return render_template('blog_page.html', blogs=blogs, res =res)

@app.route('/showblos/<int:blog_id>',methods=['GET','POST'])
def showblog(blog_id):
    blog = Blog_content.query.filter_by(id=blog_id).one()
    return render_template('showblog.html',blog = blog)

@app.route('/update_blog/<int:blogid>',methods=['GET','POST'])
def update(blogid):
    return ''





if __name__ == '__main__':
    app.run(debug=True)
