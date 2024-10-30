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
from pygetwindow import PyGetWindowException, BaseWindow

LOGGER_ENABLE = True
TEST_MODE = False

logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)
# 创建一个处理器，用于写入日志文件
fh = logging.FileHandler('testpy_script.log')
fh.setLevel(logging.DEBUG)
# 添加到 logger 中
logger.addHandler(fh)

def log(*content, **kwargs):
    level = int(kwargs.get('level', logging.INFO))
    now = datetime.datetime.now()
    if LOGGER_ENABLE:
        for each in content:
            logger.log(level, f'[{now}] {each}')
    print(*content)

def handle_exception(exc_type, exc_value, exc_traceback):
    now = datetime.datetime.now()
    # 将异常信息写入日志
    logger.error(f"[{now}] Uncaught exception",
                  exc_info=(exc_type, exc_value, exc_traceback))

# 设置全局异常处理
#sys.excepthook = handle_exception

class BaseScript:
  def __init__(self, idx=0):
    self.idx = idx

  def do(self):
        pass
  
def mySleep(second):
    random_increase = random.uniform(0.1, 1)
    sec = max(0, second)
    sec += random_increase*sec
    time.sleep(sec)

def pRand(n, p, dan=False):
    if p <0 :
        p = -p
    if dan == True:
        random_increase = random.uniform(0, p)
        n += random_increase*n
    else:
        random_increase = random.uniform(-p, p)
        n += random_increase*n
    return n

# 窗口固定大小
originSize = [1040, 807]
smallSize = (907, 707)
# 鼠标到变化态需要向做微调距离
frameSize = [0, 0]

class Frame:
    left = 0
    top = 0
    right = 0
    bottom = 0

    def __init__(self, left, top):
        self.left = left
        self.top = top

    def __str__(self):
        return "left:" + str(self.left) + " top:" + str(self.top) + " right:" + str(self.right) + " bottom:" + str(
            self.bottom)
# 窗口左上侧位置 init后修改
frame = Frame(0, 0)

# def locateCenterOnScreen(pic, region=None, confidence=0.9):
#     if region is None:
#         region = (frame.left, frame.top, frameSize[0], frameSize[1])
#     cfd = confidence if Util.__openCVEnable() else None
#     if isinstance(pic, list):
#         res = None
#         for i in pic:
#             if cfd is not None:
#                 res = pyautogui.locateCenterOnScreen(i, region=region, confidence=cfd)
#             else:
#                 res = pyautogui.locateCenterOnScreen(i, region=region)
#             if res is not None:
#                 return res
#         return res
#     else:
#         if cfd is not None:
#             return pyautogui.locateCenterOnScreen(pic, region=region, confidence=cfd)
#         else:
#             return pyautogui.locateCenterOnScreen(pic, region=region)