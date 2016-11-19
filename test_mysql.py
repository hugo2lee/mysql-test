import time
from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from utils import log, now

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost:3306/codee?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
manager = Manager(app)


class ModelHelper(object):
    def __repr__(self):
        """
        __repr__ 是一个魔法方法
        简单来说, 它的作用是得到类的 字符串表达 形式
        比如 print(u) 实际上是 print(u.__repr__())
        """
        classname = self.__class__.__name__
        properties = ['{}: ({})'.format(k, v) for k, v in self.__dict__.items()]
        s = '\n'.join(properties)
        return '< {}\n{} \n>\n'.format(classname, s)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class User(db.Model, ModelHelper):
    __tablename__ = 'user'
    # 下面是字段定义
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40))
    password = db.Column(db.String(40))
    avatar = db.Column(db.String(40))
    created_time = db.Column(db.String(40), default=0)

    def __init__(self, form):
        self.username = form.get('username', '')
        self.password = form.get('password', '')
        self.avatar = form.get('avatar', 'http://vip.cocode.cc/uploads/avatar/default.png')
        self.created_time = now()


def add_some():
    form = {
        'username': 'hugo',
        'password': '123',
        'avatar': 'hugo post',
    }
    user = User(form)
    user.save()
    log('add user')


def find_item(item):
    user = User.query.filter_by(password=item).all()
    log(user)


def db_build():
    db.drop_all()
    db.create_all()
    log('rebuild database')


def test():
    # db_build()
    # manager.run()
    add_some()
    # find_item('123')

if __name__ == '__main__':
    test()



