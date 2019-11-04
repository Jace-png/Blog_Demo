# index 接口文件
from flask import Flask, request, render_template, flash
import longin
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis

app = Flask(__name__)  # Flask对象app
app.register_blueprint(longin.bp)  # 注册蓝图对
app.secret_key = 'asdfasdfas'  #设置会话密钥

redis = StrictRedis(host='localhost', port=6379, db=0)

#mysql 配置
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root:jace666@localhost/pythonclass"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'userall'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(12), unique=True)
    password = db.Column(db.String(20), unique=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):  # 重写repr方法
        return "{'User':%s ,'Pwd': %s}" % (self.username,self.password)


# db.create_all()  #创建数据库


@app.route('/user_register', methods=['GET', 'POST'])   #注册
def longin_judge():
    if request.method == 'POST':

        username = request.form['Newusername']
        upwd = request.form['Newupwd']
        upwd2 = request.form['Newupwd2']
        print(username)
        print(type(username))
        if 10<=len(username)<=12 and 8<=len(upwd)<=15 and upwd == upwd2 and username !=upwd:
            add_user = User(username,upwd)
            print(add_user)
            db.session.add(add_user)
            db.session.commit()
            return render_template('login.html')
        else:
            flash('注册失败!请注意格式和长度')
            return render_template('register_file.html')
    return render_template('register_file.html')



@app.route('/',methods=['GET','POST'])
def user_login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        username = request.form['username']
        userpwd = request.form['pwd']

        user = User.query.filter(User.username == username).all()
        for i in user:
            # print(i.username,i.password)
            print(user)
            if username == i.username and userpwd == i.password:
                print(user)
                print(type(user))
                # print(user.username)
                return  render_template('blog_home.html')
            else:
                return render_template('login.html')







# @app.route('/registuser', methods=['GET', 'POST'])
# def regist_judge():
#     if request.method == "GET":
#         return render_template('register_file.html')
#     else:
#         flash('注册失败!请注意格式和长度')
#         username=request.form['Newusername']
#         pwd = request.form['Newupwd']
#         pwd2 = request.form['Newupwd2']
#         if pwd == pwd2 and 10<=len(pwd)>=11 and 10<=len(pwd2)>=12 and username != pwd:
#             res = redis.set(str(username),str(pwd))
#             # print(res)
#             # print(type(res))
#             return render_template('blog_home.html')
#         else:
#             return render_template('register_file.html')




if __name__ == '__main__':
    app.run(debug=True)
