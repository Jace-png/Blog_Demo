from flask import Flask
from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,DateTimeField,TextAreaField
from flask_wtf.file import FileAllowed, FileRequired, FileField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
import auto


app = Flask(__name__)
app.secret_key = 'asdfasdfas'
app.register_blueprint(auto.bp)


#mysql配置
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root:jace666@localhost/pythonclass"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)  #mysql对象  db


class MyFrom(FlaskForm):      #表单的样子
    title = StringField('Title',validators=[DataRequired()])
    fname = FileField('FileName', validators=[FileAllowed(['jpg', 'png', 'gif','text']), FileRequired()])  # 上传文件
    submit = SubmitField('upload',validators=[DataRequired()])
    AllFile = TextAreaField('Blog content',validators=[DataRequired()])

    # del_but = SubmitField('DeleteFile')  # 删除文件

class Blog_content(db.Model):  # 博客内容
    __tablename__ = 'bolgs'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    AuTo = db.Column(db.String(10),unique=False)
    FileName = db.Column(db.String(50), unique=False)
    Title = db.Column(db.String(100),unique=False)
    Content = db.Column(db.TEXT,unique=False,nullable=False)
    Blog_file_info = db.Column(db.Integer, db.ForeignKey('UserAll.id'))
    form_info = db.relation('User',backref='FileAll')

    def __init__(self, AuTo, FileName,Content,Title,Blog_file_info):
        self.AuTo = AuTo
        self.FileName = FileName
        self.Content = Content
        self.Title = Title
        self.Blog_file_info = Blog_file_info

    # def __repr__(self):  # 重写repr方法
    #     return "{'AuTo':%s ,'FileName': %s,'FileStyle':%s,'Content':%s,'Id':%s}" % \
    #            (self.AuTo, self.FileName,self.FileStyle,self.Content,self.id)



class User(db.Model):  # 用户表
    __tablename__ = 'UserAll'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    nickname = db.Column(db.String(12),unique=True)
    username = db.Column(db.String(12), unique=True)
    password = db.Column(db.String(33), unique=False)
    form_info = db.relation('Blog_content', backref='UserAll')

    def __init__(self,nickname,username, password):
        self.nickname = nickname
        self.username = username
        self.password = password

    # def __repr__(self):  # 重写repr方法
    #     return "{'id':%s,'Nickname':%s,User':%s ,'Pwd': %s}" % (self.id,self.nickname,self.username, self.password)

# db.create_all()



