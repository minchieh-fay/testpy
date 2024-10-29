import functools
import datetime
import json
import logging
import sys
import threading
import time
import random
import playsound as pl
import pyautogui
import pydirectinput
import pyperclip
from PIL import Image

from pygetwindow import PyGetWindowException, BaseWindow

import tool

def diag_func_print(self):
  print(self.left, self.width, self.height, self.right)

def __openCVEnable():
        __openCVEnable = True
        try:
            import cv2
        except ImportError:
            __openCVEnable = False
        return __openCVEnable

def fullImge(pic):
    return "img/"+pic+".png"

def locateCenterOnScreen(self, pic, reg=33, confidence=0.9):
    pic = fullImge(pic)
    region = (self.left, self.top, self.width, self.height)
    reg_shi = reg // 10
    if reg_shi == 1:
        region = (self.left, self.top, self.width//2, self.height)
    if reg_shi == 2:
        region = (self.left+(self.width//2), self.top, self.width//2, self.height)
    reg_ge = reg % 10
    if reg_ge == 1:
        region = (self.left, self.top, self.width, self.height//2)
    if reg_ge == 2:
        region = (self.left, self.top+(self.height//2), self.width, self.height//2)

    # 如果reg的尾数是0, 那么region的高度减少一半
    if reg % 10 == 0:
        region = (self.left, self.top, self.width, self.height//2)
    cfd = confidence if __openCVEnable() else None
    if isinstance(pic, list):
        res = None
        for i in pic:
            if cfd is not None:
                res = pyautogui.locateCenterOnScreen(i, region=region, confidence=cfd)
            else:
                res = pyautogui.locateCenterOnScreen(i, region=region)
            if res is not None:
                return res
        return res
    else:
        if cfd is not None:
            return pyautogui.locateCenterOnScreen(pic, region=region, confidence=cfd)
        else:
            return pyautogui.locateCenterOnScreen(pic, region=region)
        
def locateCenterOnScreen_safe(self, pic, reg=33, confidence=0.9):
    try:
        return self.locateCenterOnScreen(pic, reg, confidence)
    #except PyGetWindowException:
    except Exception as e:
        return None

def locateCenterOnScreen_ex(self, pic, reg=33, confidence=0.9, timeDue=2):
    res = self.locateCenterOnScreen_safe(pic, reg, confidence)
    if res is None:
        return res
    tool.mySleep(timeDue)
    return self.locateCenterOnScreen_safe(pic, reg, confidence)

def leftClickImg(self, pic, reg=33, confidence=0.9, yfix=0, xfix=0, timeDue=2) -> bool:
    res = self.locateCenterOnScreen_ex(pic, reg, confidence, timeDue)
    if res is None:
        print("图片未找到", pic)
        return False
    pic = fullImge(pic)
    image = Image.open(pic)
    w, h = image.size
    w = w - xfix
    h = h - yfix
    w_rand = random.randint(int(-w/4), int(w/4))
    h_rand = random.randint(int(-h/4), int(h/4))
    pyautogui.leftClick(res[0]+int(xfix/2)+w_rand, res[1]+int(yfix/2)+h_rand)
    return True

def diag_func(d):
  d.xxx = functools.partial(diag_func_print, d)
  # 获取图片在窗口的位置
  d.locateCenterOnScreen = functools.partial(locateCenterOnScreen, d)
  # 获取图片在窗口的位置，如果失败，则返回None
  d.locateCenterOnScreen_safe = functools.partial(locateCenterOnScreen_safe, d)
  # 获取图片在窗口的位置，隔2s后再次获取, 以免第一次运动中的按钮//如宝图
  d.locateCenterOnScreen_ex = functools.partial(locateCenterOnScreen_ex, d)
  # 点击图片
  d.leftClickImg = functools.partial(leftClickImg, d)
  