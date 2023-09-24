import RPi.GPIO as GPIO
import time
import requests



# 设置GPIO模式为BOARD
GPIO.setmode(GPIO.BOARD)

# 设置LED引脚
led = 11
GPIO.setup(led, GPIO.OUT)

while True :
     response = requests.get(url='http://c0.veypi.com/status')
     a = response.text

     if  a == '1'  :
        GPIO.output(led,GPIO.HIGH)

     if  a == '0'  :
        GPIO.output(led,GPIO.LOW)

# 清理GPIO设置
GPIO.cleanup()
/***



***/
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
