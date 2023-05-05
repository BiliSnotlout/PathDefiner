import turtle
import time
import win32clipboard
import pyautogui
import keyboard
def clip(text, target):
    """
    将内容输入到Windows剪贴板, 然后在服务端打印出来
    """
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(text)
    win32clipboard.CloseClipboard()
    app_window = pyautogui.getWindowsWithTitle(target)[0]
    app_window.activate()
    keyboard.press('ctrl')
    keyboard.press('v')
    keyboard.release('v')
    keyboard.release('ctrl')
    keyboard.press('enter')
    keyboard.release('enter')
    keyboard.press('enter')
    keyboard.release('enter')

def draw_bezier_curve(pos0, pos1, pos2, pos3, s):
    """
    绘制三次贝塞尔曲线(控制点为p1, p2; 出入点为p0, p3)
    """
    t = 0.0
    while t < 1.0:
        #计算值
        x = (1-t)**3 * pos0[0] + 3*t*(1-t)**2 * pos1[0] + 3*t**2*(1-t) * pos2[0] + t**3 * pos3[0]
        y = (1-t)**3 * pos0[1] + 3*t*(1-t)**2 * pos1[1] + 3*t**2*(1-t) * pos2[1] + t**3 * pos3[1]
        z = (1-t)**3 * pos0[2] + 3*t*(1-t)**2 * pos1[2] + 3*t**2*(1-t) * pos2[2] + t**3 * pos3[2]
        text = ("tp {} {} {} {}".format(playername, x+shift[0], y+shift[1], z+shift[2]))
        clip(text, target)
        #准备下一次循环
        print(t)
        turtle.goto(x, z)
        time.sleep(0.1)
        t += 0.1 / s

# 键入区
target = "Bedrock"#服务端窗口的名字
playername = "BiliSnotlout"#录影账号的名字
shift = (0, 0, 0) # 坐标系的原点

# 坐标（奇数列为柄角度, 偶数列为节点位置）
posx = [80, 80, 40, 0, -80, -80, -40, 0, 80, 80]
posy = [80, 80, 80, 80, 80, 80, 80, 80, 80, 80]
posz = [-40, 0, 80, 80, 40, 0, -80, -80, -40, 0]

#柄长度（柄会影响线段的曲率）
pro = [1, 1, 1, 1, 1, 1, 1, 1]

#时间
sec = 10
rdy = 3
s = sec/(len(posx)/2-1)
"""
全部都是0的表格, 复制用
posx = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
posy = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
posz = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
"""

#创建变量
pos0 = (0, 0, 0)
pos1 = (0, 0 ,0)
pos2 = (0, 0 ,0)
pos3 = (0, 0, 0)

#初始化turtle
turtle.speed(0)
turtle.penup()
turtle.goto(shift[0], shift[2])
turtle.pendown()

#预备
text = ("title @a title {}s".format(rdy))
clip(text, target)
time.sleep(0.05)
text = ("title @a subtitle Prepare for recording")
clip(text, target)
for i in range(rdy):
    time.sleep(1)

# 循环拉取坐标和柄绘制贝塞尔曲线, 直到坐标列表的倒数第二项
for i in range(len(posx)//2-1):
    pos0 = (posx[i*2+1], posy[i*2+1], posz[i*2+1])
    pos1 = ((posx[i*2+1] + (posx[i*2+1] - posx[i*2])) * pro[i], (posy[i*2+1] + (posy[i*2+1] - posy[i*2])) * pro[i], (posz[i*2+1] + (posz[i*2+1] - posz[i*2])) * pro[i])
    pos2 = (posx[i*2+2], posy[i*2+2], posz[i*2+2])
    pos3 = (posx[i*2+3], posy[i*2+3], posz[i*2+3])
    print (pos0, pos1, pos2, pos3, sec, pro[i])
    draw_bezier_curve(pos0, pos1, pos2, pos3, s)

text = ("title @a title finished")
clip(text, target)
turtle.done()