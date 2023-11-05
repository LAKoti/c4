import random
import asyncio
import tornado

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
        (r"/random", randomTest),
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

