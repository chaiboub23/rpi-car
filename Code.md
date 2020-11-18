# Code Documentation

The code is located in *main.py*. It isn't a big file, due to the simplicity of the explorerhat module. To download it, use curl.
```bash
curl https://get.pimoroni.com/explorerhat | bash
```
Next, you want to import it in your python file.
```python
import explorerhat
```
You should also import the time module.
```python
import time
```
Next, we made functions for each direction the car can go in.
```python
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
```
The `explorerhat.motor.forwards` and `explorerhat.motor.backwards` move both motors forwards and backwards respectively.
Adding either one or two between motor and the direction moves either the first or second motor in the respective direction. A combination of them moving in opposite directions moves the car either right or left. Adding stop makes the motors stop.

Next, there is a while loop to enter all the commands during the period in which the file is run.
```python
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
```
This makes sure you can control the car with the "WASD" keys and stop with the "3" key. This loops until another character is entered. To make sure the user knows the controls, a message is printed:
```python
print("w=forward,s=backward,a=left,d=right,3=stop")
```
