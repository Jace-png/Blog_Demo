from flask import Flask
from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,DateTimeField
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
    Autoname = StringField('AUTO',validators=[DataRequired()])
    fname = FileField('FileName', validators=[FileAllowed(['jpg', 'png', 'gif','text']), FileRequired()])  # 上传文件
    sub_time = DateTimeField('SubmitTime')
    submit = SubmitField('upload')

    # del_but = SubmitField('DeleteFile')  # 删除文件







class File(db.Model):  # 文件表
    __tablename__ = 'FileAll'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    AuTo = db.Column(db.String(10),unique=True)
    FileName = db.Column(db.String(50), unique=True)
    FileStyle = db.Column(db.String(20), unique=False)
    SubmitTime = db.Column(db.String(100),unique=False)
    blog_file_info = db.Column(db.Integer, db.ForeignKey('UserAll.id'))

    form_info = db.relation('User',backref='FileAll')

    def __init__(self, AuTo, FileName,FileStyle,SubmitTime,blog_file_info):
        self.AuTo = AuTo
        self.FileName = FileName
        self.FileStyle = FileStyle
        self.SubmitTime = SubmitTime
        self.blog_file_info = blog_file_info

    def __repr__(self):  # 重写repr方法
        return "{'AuTo':%s ,'FileName': %s,'FileStyle':%s,'SubmitTime':%s}" % (self.AuTo, self.FileName,self.FileStyle,self.SubmitTime)



class User(db.Model):  # 用户表
    __tablename__ = 'UserAll'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    username = db.Column(db.String(12), unique=True)
    password = db.Column(db.String(20), unique=False)
    form_info = db.relation('File', backref='UserAll')

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):  # 重写repr方法
        return "{'id':%s,'User':%s ,'Pwd': %s}" % (self.id,self.username, self.password)

# db.create_all()



