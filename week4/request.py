#! /usr/bin/env python3
# vim:fenc=utf-8
#
# Copyright © 2023 veypi <i@veypi.com>
#
# Distributed under terms of the MIT license.

"""

"""

import requests

response = requests.post(url='http://127.0.0.1:8888/data',
                         data={'io': '123123'})
print([response.text])
