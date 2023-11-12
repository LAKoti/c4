#! /usr/bin/env python3
# vim:fenc=utf-8
#
# Copyright © 2023 veypi <i@veypi.com>
#
# Distributed under terms of the MIT license.

import asyncio
import tornado
import random
import time

''''''
from sqlalchemy import Column, String, create_engine, select, Float, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql
pymysql.install_as_MySQLdb()
# 创建对象的基类:
Base = declarative_base()
status = '0'
class ToggleHandler(tornado.web.RequestHandler):
    def get(self):
        global status
        if status == '1':
            status = '0'
        else:
            status = '1'
        self.write(status)
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("""hello world""")
data = ''
"""
class DataHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(data)

    def post(self):
        global data
        io = self.get_argument('io')
        data = data + io
        print(data)
        self.write("ok")
"""
'''
class DataHand(tornado.web.RequestHandler):
    def get(self):
        self.write(data)

    def post(self):
        global data
        io = self.get_query_argument('io', default='nothing')
        print(io)
        data = data + io
        engine = create_engine('mysql+mysqlconnector://root:AstralEcho@c4.veypi.com:3306/test_c4')

        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        new_user = User(id=data)
        session.add(new_user)
        session.commit()
        session.close()

        self.write('okkkk')
'''

html_text="""
<!DOCTYPE html>
<html>
    <body>
        <h2>收到Get请求</h2>
        <form method='post'>
            <input type='text' name='name' placeholder='输入心率数据:'/>
            <input type='submit' value='上传数据'/>
        </form>
    </body>
</html>
"""
class DataHandler(tornado.web.RequestHandler):
    def get(self):  # 定义请求函数
        self.write(html_text)

    def post(self):
        name = self.get_argument('name', default='0', strip=True)
        a = time.time()
        b = int(name)

        self.write('上传的数据：%s' % name)
        self.write('   %s' % str(a))

        # 创建对象的基类:
        Base = declarative_base()

        # 定义User对象:
        class User(Base):
            # 表的名字:
            __tablename__ = 'heart'
            # 表的结构:
            time = Column(Float, primary_key=True)
            rate = Column(Integer)

        # 初始化数据库连接:
        engine = create_engine('mysql+mysqlconnector://root:AstralEcho@c4.veypi.com:3306/zys')
        # 创建DBSession类型:
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        new_user = User(time=a, rate=b)
        # 添加到session:
        session.add(new_user)
        # 提交即保存到数据库:
        session.commit()
        # 关闭session:)
        session.close()

class StatusHandler(tornado.web.RequestHandler):
    def get(self):
        global status
        self.write(status)
class hello(tornado.web.RequestHandler):
    def get(self):
        self.write("helloworld")
###
i1 = 1
class item1(tornado.web.RequestHandler):
    def get(self):
        global i1
        i1 += 1
        self.write(str(i1))
###
i2 = 1
class item2(tornado.web.RequestHandler):
    def get(self):
        global i2
        global i1
        i = i2
        i2 = i2 + i1
        i1 = i
        self.write(str(i2))
###
i3 = 0
class item3(tornado.web.RequestHandler):
    def get(self):
        global i3
        i3 += 1
        i3 += i2
        self.write(str(i3))
'''
def send_data(num):
    a=[]
    for i in range(num):
        a.append([i,round(np.random.normal(90,0.50))])
    return a
class randomHandler(tornado.web.RequestHandler):
    def get(self):
        a=send_data(100)
        self.write(str(a))
'''
def listing():
    # global item
    item = random.gauss(90, 0.5)
    return str(item)
    # self.write(str(item))
class randomTest(tornado.web.RequestHandler):
    def get(self):
        global list_2d
        list_2d = [[]]
        for i in range(100):
            list_2d.append([])
            p = str(listing())
            list_2d[i].append(p)
            list_2d[i].append(i)
        self.write(str(list_2d))
listRead = [[]]
#Base = declarative_base()
class User(Base):
    # 表的名字:
    __tablename__ = 'heart'

    # 表的结构:

    id = Column(Integer, primary_key=True, autoincrement=True)
    time = Column(Float)
    rate = Column(Integer)
#def read_from_SQL :
class readFromSQL(tornado.web.RequestHandler):
    def get(self):
        global listRead

        engine = create_engine('mysql+mysqlconnector://root:AstralEcho@c4.veypi.com:3306/zys')


        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        all = session.query(User).all()
        resdata = []
        for a in all:
            resdata.append([a.time, a.rate])
            print("%s %s"%(a.time, a.rate))
        #new_user = User(time=time.time(), rate=000)
        #s1 = select([User.time])
        #s2 = select([User.rate])
        self.write(str(resdata))

        session.close()

def make_app():
    return tornado.web.Application([
        # (r"/", MainHandler),
        (r"/helloworld", hello),
        (r"/random", randomTest),
        (r"/item1", item1),
        (r"/item2", item2),
        (r"/item3", item3),
        (r"/read", readFromSQL),
        (r"/DataHandler", DataHandler),
        (r"/home/(.*)", tornado.web.StaticFileHandler, {"path": "./home.html"}),
        (r"/(.*)", tornado.web.StaticFileHandler, {"path": "./index.html"}),
    ])
async def main():
    app = make_app()
    port = 8888
    app.listen(port)
    print("start srv on %d" % port)
    await asyncio.Event().wait()
if __name__ == "__main__":
    asyncio.run(main())
