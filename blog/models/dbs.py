from datetime import datetime

from blog.conf.export import db


class BaseModel(db.Model):
    extend_existing = True
    __abstract__ = True
    __table_initialized__ = False
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    create_time = db.Column(db.DateTime, default=datetime.now(), comment="创建时间")
    update_time = db.Column(db.DateTime, comment="更新时间")

    @classmethod
    def get(cls, filters, entities):
        fields = entities if isinstance(entities, list) else [cls]
        return db.session.query(*fields).filter(*filters)


class Blog(BaseModel):  # 博客内容
    __tablename__ = 'blog'
    auto = db.Column(db.String(10), unique=False)
    filename = db.Column(db.String(50), unique=False)
    title = db.Column(db.String(100), unique=False)
    content = db.Column(db.TEXT, unique=False, nullable=False)
    file_info = db.Column(db.Integer, db.ForeignKey('UserAll.id'))
    form_info = db.relation('User', backref='FileAll')


class User(BaseModel):  # 用户表
    __tablename__ = 'user'
    nickname = db.Column(db.String(12), unique=True)
    username = db.Column(db.String(12), unique=True)
    password = db.Column(db.String(33), unique=False)

# db.create_all()
