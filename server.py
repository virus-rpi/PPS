import sys
import os
import socket
import win32con
from flask import Flask, request
import json
import ctypes
import win32gui

app = Flask(__name__)

with open('settings.json') as json_file:
    settings = json.load(json_file)

pin = 0


def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


def switch():
    if pin == 0:
        virtual_desktop_accessor = ctypes.WinDLL(resource_path("VirtualDesktopAccessor.dll"))
        virtual_desktop_accessor.GoToDesktopNumber(1)


def minimize():
    if pin == 0:
        hWnd = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(hWnd, win32con.SW_MINIMIZE)


def action(args):
    global pin
    id = args["id"]
    pin = args["pin"]
    if settings[str(id)] == "s":
        switch()
    elif settings[str(id)] == "m":
        minimize()


@app.route('/', methods=['POST'])
def result():
    req = request.data.decode("utf-8")
    action(eval(req))
    return 'Received!'


app.run(host=socket.getaddrinfo(socket.gethostname(), None)[-1][-1][0])
