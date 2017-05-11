#!/usr/bin/python2
#coding:utf-8
import RPi.GPIO as GPIO
import time
dc = 30
GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

p1=GPIO.PWM(15,50)
p1.start(0)
p1.ChangeDutyCycle(dc)

p2=GPIO.PWM(18,50)
p2.start(0)
p2.ChangeDutyCycle(dc)

GPIO.setup(11, GPIO.OUT)
# 初始化设置引脚输出
def init():
        GPIO.setup(11, GPIO.OUT)
        GPIO.setup(13, GPIO.OUT)

        GPIO.setup(12, GPIO.OUT)
        GPIO.setup(16, GPIO.OUT)


# 所有引脚置低电平，用于复位、停止运行的功能
def reset():
        GPIO.output(11, GPIO.LOW)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(12, GPIO.LOW)
        GPIO.output(16, GPIO.LOW)
# back
def front_left_forward():
        GPIO.output(11, GPIO.HIGH)
        GPIO.output(13, GPIO.LOW)

        GPIO.output(12, GPIO.HIGH)
        GPIO.output(16, GPIO.LOW)
# front
def front_right_forward():
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(11, GPIO.LOW)

        GPIO.output(16, GPIO.HIGH)
        GPIO.output(12, GPIO.LOW)

# 停止
def stop():
        reset()
# 测试各个功能点
if __name__ == "__main__":
        init()
        reset()
        front_left_forward()
        time.sleep(3)
        stop()
        time.sleep(3)
        front_right_forward()
        time.sleep(3)
        stop()
        GPIO.cleanup()
