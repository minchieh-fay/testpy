import pyautogui
import random

from PIL import Image

from diag import *
from diag_func import *

print("Hello World!")

if __name__ == '__main__':
  print("Run mi and tu!")
  # 死循环for, 每过5秒打印hello
  diags = getWindowList()

  if len(diags) != 2:
    print("diag not right")
    sys.exit(1)
  
  while True:
    for diag in diags:
      mySleep(5)
      diag.leftClickImg("test", yfix=50)
      mySleep(5)
      diag.leftClickImg("test", yfix=50)
