# index 接口文件
from flask import Flask,session,escape
from flask import request, render_template, flash, redirect
from dbs import MyFrom,db,User,app,File
import base64




@app.route('/user_register', methods=['GET', 'POST'])  # 注册
def longin_judge():
    if request.method == 'POST':
        username = request.form['Newusername']
        upwd = request.form['Newupwd']
        upwd2 = request.form['Newupwd2']
        print(username)
        print(type(username))
        if 10 <= len(username) <= 12 and 8 <= len(upwd) <= 15 and upwd == upwd2 and username != upwd:
            res = base64.b64encode(upwd.encode('utf8'))
            print(res)
            add_user = User(username, res)
            print(add_user)
            db.session.add(add_user)
            db.session.commit()
            return render_template('auth/login.html')
        else:
            flash('注册失败!请注意格式和长度')
            return render_template('auth/register_file.html')
    return render_template('auth/register_file.html')




@app.route('/', methods=['GET', 'POST'])  # 登陆
def user_login():
    form = MyFrom()
    if request.method == "GET":
        return render_template('auth/login.html')
    else:
        username = request.form['username']
        userpwd = request.form['pwd']
        user = User.query.filter(User.username == username).all()
        for i in user:
            # print(i.username,i.password)
            print(user)
            user_logining = i.username
            session['num'] = i.id
            dpwd = i.password
            rpwd = base64.b64decode(dpwd).decode('utf8')
            if username == i.username and userpwd == rpwd:
                # print(user)
                # print(type(user))
                # print(user.username)
                return render_template('home_site.html', form=form,user_logining=user_logining)
            else:
                return render_template('auth/login.html')




@app.route('/success', methods=['GET', 'POST'])    #homesite
def content():
    form = MyFrom()
    if request.method == 'GET':
        return render_template('home_site.html', form=form)
    else:
        if form.validate_on_submit():
            filename = form.fname.data.filename
            # print(filename)
            auto = form.Autoname.data
            sub_time = form.sub_time.data
            res = filename[-3:]
            # print(res)
            # print(auto)
            # print(sub_time)
            userid = escape(session['num'])  #session   用户表的id
            # print(userid)
            # print(type(userid))
            file_info = File(auto,filename,res,sub_time,userid)
            db.session.add(file_info)
            db.session.commit()
            form.fname.data.save('Imgs/{}'.format(filename))
            return redirect('/success')
        return render_template('home_site.html', form=form)




if __name__ == '__main__':
    app.run(debug=True)
