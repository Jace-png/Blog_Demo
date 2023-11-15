from typing import Dict
from blog.models.dbs import User
from blog.utils.public import gen_md5
from blog.conf.export import db


class UserService:

    def register(self, data: Dict):
        """用户注册
        """
        password = data.get("Newupwd")
        username = data.get("Newusername")
        nickname = data.get("Nickname")

        md5_pwd = gen_md5(password)
        user = User(nickname=nickname, username=username, password=md5_pwd)
        db.session.add(user)
        db.session.commit()
        return user
