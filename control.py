import pyautogui
import time
import keyboard
import random
import fileinput
import win32api, win32con,win32gui
import aiogram 
import logging
import requests 
from termcolor import colored 
from colorama import init 
from pyautogui import *
import datetime
import cv2,pygetwindow
from PIL import Image


class Control:

    def controller(self):
        i = input()
        Control().move(str(i))

    def check_window(self):
        #time.sleep(5)
        pyautogui.getWindowsWithTitle("VisualBoyAdvance")[0].maximize()
        CHECK = pyautogui.locateOnScreen('./pic/check.JPG', grayscale=True, confidence=0.5)
        return False if CHECK == None else True

    def move(self,msg):
        checkmove = Control().check_window()
        if checkmove == True: 
            pyautogui.getWindowsWithTitle("VisualBoyAdvance")[0].maximize()
            CHECK = pyautogui.locateOnScreen('./pic/check.JPG', grayscale=True, confidence=0.5)
            pyautogui.moveTo(CHECK) if CHECK != None else print("PASS")
            pyautogui.move(45,45,0),pyautogui.click()
            pyautogui.keyDown('z'),time.sleep(0.5),pyautogui.keyUp('z'),time.sleep(0.5) if msg == "a" else(pyautogui.keyDown('x'),time.sleep(0.5),pyautogui.keyUp('x'),time.sleep(0.5) if msg == "b" else(pyautogui.keyDown('up'),time.sleep(0.5),pyautogui.keyUp('up'),time.sleep(0.5) if msg == "up" else(pyautogui.keyDown('down'),time.sleep(0.5),pyautogui.keyUp('down'),time.sleep(0.5) if msg == "down" else(pyautogui.keyDown('left'),time.sleep(0.5),pyautogui.keyUp('left'),time.sleep(0.5) if msg == "left" else(pyautogui.keyDown('right'),time.sleep(0.5),pyautogui.keyUp('right'),time.sleep(0.5) if msg == "right" else print('pass'))))))
            Control().screenshot()



    def screenshot(self):
        window= pygetwindow.getWindowsWithTitle('VisualBoyAdvance')[0]
        x1,y1,hei,wid = window.left,window.top,window.height,window.width
        x2,y2 = x1 + wid,y1 + hei
        pyautogui.screenshot('./screen/lastmove.png')
        im = Image.open('./screen/lastmove.png')
        im = im.crop((x1,y1,x2,y2))
        im.save('./screen/lastmove.png')
        #return True
        Control().controller()

    def press_test(msg):
        pyautogui.press(str(msg))
