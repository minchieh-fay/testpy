import io
import os
from flask import Flask, send_file, send_from_directory,jsonify, request
import pyautogui
from PIL import Image
import json
import random

import tool
import diag 
#from run_mi_tu import *
import run_mi_tu

app = Flask(__name__,static_folder='www')


@app.route('/screenshot', methods=['GET'])
def screenshot():
    # 获取指定标题的窗口列表
    windows = diag.getWindowList()
    
    # 检查是否找到窗口
    if not windows:
        return "Window not found", 404
    selection = int(request.args.get('selection'))

    # 获取窗口对象
    window = windows[selection]
    
    # 将窗口设为前台（可选）
    # if window.isMinimized:
    #     window.restore()
    # window.activate()

    try:
        # 直接截取窗口的区域，不使用 activate()
        screenshot = pyautogui.screenshot(region=(window.left, window.top, window.width, window.height))
    except Exception as e:
        return f"Error capturing screenshot: {e}", 500
    
    # 将截图保存到内存中
    img_io = io.BytesIO()
    screenshot.save(img_io, 'PNG')
    img_io.seek(0)

    # 返回截图作为响应
    return send_file(img_io, mimetype='image/png')

# 用于加载静态HTML文件
@app.route('/', methods=['GET'])
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/leftclick', methods=['POST'])
def leftclick():
    data = request.json
    x = data.get('x')
    y = data.get('y')
    selection = int(data['selection'])

    windows = diag.getWindowList()
    
    # 检查是否找到窗口
    if not windows:
        return "Window not found", 404

    # 获取窗口对象
    window = windows[selection]

     # 计算绝对位置
    absolute_x = window.left + x
    absolute_y = window.top + y


    try:
        # 模拟点击
        pyautogui.click(absolute_x, absolute_y)
        return json.dumps({'status': 'success', 'absolute_x': absolute_x, 'absolute_y': absolute_y})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

#拖拽背包
@app.route('/dragpag', methods=['POST'])
def dragpag():
    data = request.json
    selection = int(data['selection'])

    windows = diag.getWindowList()
    
    # 检查是否找到窗口
    if not windows:
        return "Window not found", 404

    # 获取窗口对象
    window = windows[selection]

    try:
        pyautogui.moveTo(window.left+int(tool.pRand(553,0.1)), window.top+ int(tool.pRand(438,0.1)))
        pyautogui.dragTo(window.left+int(tool.pRand(553,0.1)), window.top+int(tool.pRand(222,0.1)), duration=0.5)
        return json.dumps({'status': 'success'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
#拖拽菜单
@app.route('/dragmenu', methods=['POST'])
def dragmenu():
    data = request.json
    selection = int(data['selection'])

    windows = diag.getWindowList()
    
    # 检查是否找到窗口
    if not windows:
        return "Window not found", 404

    # 获取窗口对象
    window = windows[selection]

    try:
        pyautogui.moveTo(window.left+int(tool.pRand(454,0.1)), window.top+ int(tool.pRand(290,0.1)))
        pyautogui.dragTo(window.left+int(tool.pRand(454,0.1)), window.top+int(tool.pRand(160,0.1)), duration=0.3)
        return json.dumps({'status': 'success'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/mitu', methods=['POST'])
def mitu():
    data = request.json
    print(data)
    isOn = data['isOn']
    bSet = data['bSet']

   # global mibaotu_running
    print("rrrrr1:", run_mi_tu.mibaotu_running)
    if bSet:
        run_mi_tu.run_mi_tu(isOn) # 设置mibaotu_running为True
    print("rrrrr3:", run_mi_tu.mibaotu_running)
    return json.dumps({'status': 'success', 'isOn': run_mi_tu.mibaotu_running, 'bSet': bSet})


if __name__ == '__main__':
    #tool.TEST_MODE = True
    app.run(host='0.0.0.0', port=5000)
