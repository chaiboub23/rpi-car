import explorerhat
import time
print("w=forward,s=backward,a=left,d=right,3=stop")
def forward():
    explorerhat.motor.stop()
    explorerhat.motor.forwards()
def backward():
    explorerhat.motor.stop()
    explorerhat.motor.backwards()
def Fone():
    explorerhat.motor.stop()
    explorerhat.motor.one.forwards()
    explorerhat.motor.two.backwards()
def Ftwo():
    explorerhat.motor.stop()
    explorerhat.motor.two.forwards()
    explorerhat.motor.one.backwards()
def stop():
    explorerhat.motor.stop()

while True:
    x = input("")
    if x == "w":
        forward()
    elif x == "s":
        backward()
    elif x == "a":
        Fone()
    elif x == "d":
        Ftwo()
    elif x == "3":
        stop()
    else:
        break
