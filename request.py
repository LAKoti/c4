#! /usr/bin/env python3
# vim:fenc=utf-8
#
# Copyright © 2023 veypi <i@veypi.com>
#
# Distributed under terms of the MIT license.

"""

"""

import requests

# 通过url直接加上请求参数，与通过params传参效果是一样的
response = requests.get(url='http://127.0.0.1:8888/status')
print([response.text])
