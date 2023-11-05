#! /usr/bin/env python3
# vim:fenc=utf-8
#
# Copyright © 2023 veypi <i@veypi.com>
#
# Distributed under terms of the MIT license.

"""

"""

import asyncio
import tornado
import random

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
class DataHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(data)

    def post(self):
        global data
        io = self.get_argument('io')
        data = data + io
        print(data)
        self.write("ok")


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
        #self.write(str(item))

class randomTest(tornado.web.RequestHandler):
    def get(self):
        global list_2d
        list_2d = [[]]
        for i in range(100):
            list_2d.append([])
            p=str(listing())
            list_2d[i].append(p)
            list_2d[i].append(i)
        self.write(str(list_2d))
def make_app():
    return tornado.web.Application([
        # (r"/", MainHandler),
        (r"/helloworld", hello),
        (r"/random",randomTest),
        (r"/item1",item1),
        (r"/item2",item2),
        (r"/item3",item3),
        (r"/home/(.*)",tornado.web.StaticFileHandler,{"path":"./home.html"}),
        (r"/(.*)",tornado.web.StaticFileHandler,{"path":"./index.html"}),
    ])

async def main():
    app = make_app()
    port = 8888
    app.listen(port)
    print("start srv on %d"%port)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())


