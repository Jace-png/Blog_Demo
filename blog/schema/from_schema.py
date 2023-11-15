from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField
from flask_wtf.file import FileAllowed, FileRequired, FileField
from wtforms.validators import DataRequired


class MyFrom(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    name = FileField('FileName', validators=[FileAllowed(['jpg', 'png', 'gif', 'text']), FileRequired()])  # 上传文件
    submit = SubmitField('upload', validators=[DataRequired()])
    AllFile = TextAreaField('Blog content', validators=[DataRequired()])
