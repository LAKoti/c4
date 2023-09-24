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

class StatusHandler(tornado.web.RequestHandler):
    def get(self):
        global status
        self.write(status)

def make_app():
    return tornado.web.Application([
        # (r"/", MainHandler),
        (r"/toggle", ToggleHandler),
        (r"/status", StatusHandler),
        (r"/(.*)", tornado.web.StaticFileHandler, {"path": "./index.html"}),
    ])

async def main():
    app = make_app()
    port = 80
    app.listen(port)
    print("start srv on %d"%port)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())


