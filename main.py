# This is a sample Python script.
import os
import time

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.
# print(os.environ.get("ADB_SCRIPT_PACKAGE_ID"))
from keymap import keycodes
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class AdbHandler:
    "Common handler for adb bridge"
    start_app = "adb shell am start -n " + os.environ["ADB_SCRIPT_PACKAGE"]
    clear_app = "adb shell pm clear " + os.environ["ADB_SCRIPT_PACKAGE"]
    username = os.environ["ADB_SCRIPT_USERNAME"]
    password = os.environ["ADB_SCRIPT_PASSWORD"]
    pin = "1111"
    up = 19
    down = 20
    left = 21
    right = 22
    ok = 66
    exit = 3
    back = 4


    def __init__(self):
        print ("ADB Handler started")
        # print(AdbHandler.start_app)
    def runCommand(self, command):
        print("Running command ", command)
        cmd = "adb shell input keyevent " + str(command)
        print(cmd)
        os.system(cmd)
    def sleep(self,sec):
        print("putting to sleep for ",sec)
        time.sleep(sec)
    def enterText(self,text):
        print("Entering text ", text)
        cmd = "adb shell input text " + str(text)
        print(cmd)
        os.system(cmd)
    def runCommandMultipleTimes(self, command, n, timeout):
        print("Running command multiple times ", command, "times", n)
        for x in range(n):
            print('sending keyevent ', command)
            adb.runCommand(command)
            adb.sleep(timeout)


adb = AdbHandler()
adb.runCommand(AdbHandler.exit)
adb.sleep(2)
os.system(AdbHandler.clear_app)
os.system(AdbHandler.start_app)

adb.sleep(15)
adb.runCommandMultipleTimes(AdbHandler.ok, 8, 3)
adb.runCommand(AdbHandler.down)
adb.runCommand(AdbHandler.ok)
adb.enterText(AdbHandler.username)
adb.runCommand(AdbHandler.ok)

adb.sleep(5)

adb.runCommand(AdbHandler.back)
adb.runCommand(AdbHandler.left)
adb.runCommand(AdbHandler.down)
adb.runCommand(AdbHandler.ok)
adb.enterText(AdbHandler.password)
adb.runCommand(AdbHandler.ok)

adb.sleep(5)

adb.runCommand(AdbHandler.down)
adb.runCommand(AdbHandler.ok)

adb.sleep(2)

adb.runCommand(AdbHandler.ok)
adb.runCommand(AdbHandler.ok)

adb.sleep(2)

adb.enterText(AdbHandler.pin)
adb.runCommand(AdbHandler.ok)

adb.sleep(5)

adb.runCommand(AdbHandler.right)
adb.runCommand(AdbHandler.ok)

adb.sleep(5)

adb.runCommandMultipleTimes(AdbHandler.ok, 2, 2)
adb.runCommand(AdbHandler.right)
adb.runCommand(AdbHandler.ok)
adb.runCommandMultipleTimes(AdbHandler.down, 11, 0.5)
adb.runCommandMultipleTimes(AdbHandler.ok, 2,2)
adb.runCommandMultipleTimes(AdbHandler.back, 2,2)
