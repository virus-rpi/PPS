import requests


ID = 0

pin = int(input()) #machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
old_pin = pin  #.value()

while True:
    pin = input()
    if old_pin != pin:
        r = requests.post("http://127.0.0.1:5000", data={ID: pin})
    old_pin = pin #.value()
