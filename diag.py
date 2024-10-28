import argparse
import pyautogui


from tool import *
from diag_func import *

windowsList = None
def getWindowList():
    global windowsList
    if windowsList is not None:
        return windowsList
    windowsList = pyautogui.getWindowsWithTitle('梦幻西游：时空')
    #windowsList = pyautogui.getWindowsWithTitle('Calculator')
    windowsList = list(filter(lambda x: x.left >= 0, windowsList))
    windowsList.sort(key=lambda x: (x.left, x.top))

    if windowsList is None:
        print("没有找到窗口")
        mySleep(10)
        sys.exit(1)

    diagmove()

    for item in windowsList:
        diag_func(item)

    return windowsList

def diagmove():
    size = smallSize
    winList = getWindowList()
    sz = pyautogui.size()
    x0 = size[0] - 15
    l = int((sz.width - 2 * x0) / 2)
    zhuomianban = (l, l + x0, l, l + x0, int((sz.width - size[0]) / 2))
    i = 0
    
    for idx, item in enumerate(winList):
        log(item)
        item.resizeTo(size[0], size[1])
        mySleep(1)
        if idx == 4:
            item.moveTo(zhuomianban[4], int((sz.height - size[1]) / 2))
        else:
            # 这里任务栏写死36
            no2LineTop = (sz.height - size[1] - 36 if sz.height - size[1] * 2 < 0 else size[1]) * int(i / 2)
            item.moveTo(zhuomianban[i], no2LineTop)
            i += 1
        log("处理后：", item)


if __name__ == '__main__':
    diagmove()