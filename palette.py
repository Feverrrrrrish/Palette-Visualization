from haishoku.haishoku import Haishoku
# 配色库
import tkinter as tk
from PIL import ImageTk,Image
# UI

fp = '/demo/01.jpg'
# 路径 需修改

def rgbTo16(a):
    s = hex(a)
    if len(s) == 3:
        ss = '0' + s[2]
    else:
        ss = s[-2:]
    sss = str.upper(ss)
    return sss
# 16进制

def toPalette(palette):
    colorF = ''
    color16 = []
    for i in range(len(palette)):
        color = []
        for j in range(3):
            color.append(rgbTo16(palette[i][1][j]))
        color16.append('#'+color[0]+color[1]+color[2])
        colorF = colorF+'"'+color16[i]+'", '

    colorF = colorF[:-2]
    colorF = 'myPalette<- c('+colorF+')'
    return colorF
# R中调色盘格式

def get_screen_size(window):
    return window.winfo_screenwidth(), window.winfo_screenheight()

def get_window_size(window):
    return window.winfo_reqwidth(), window.winfo_reqheight()

def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2-80)
    window.geometry(size)

def myNewSize(a1):
    width=a1.size[0]
    height=a1.size[1]
    while (width > 500 or height > 500):
        width = 0.9*width
        height = 0.9*height
    return width,height
# 窗口居中

palette = Haishoku.getPalette(fp)
palette2 = Haishoku.getPalette2(fp)
#导入

palettePic1 = Haishoku.showPalette(fp)
palettePic2 = Haishoku.showPalette2(fp)
# 配色可视化

colorF=toPalette(palette)
colorF2=toPalette(palette2)

window = tk.Tk()
window.title('调色盘')
window.configure(background='#323232')

pic = Image.open(fp)
[w,h]=myNewSize(pic)
pic = pic.resize((int(w), int(h)), Image.ANTIALIAS)

photo = ImageTk.PhotoImage(pic)
label1 = tk.Label(window,image = photo,width = w,height = h+30,bg='#323232')
label1.pack(side=tk.TOP)

palettePhoto1 = ImageTk.PhotoImage(palettePic1)
label2 = tk.Label(window,image = palettePhoto1,bg='#323232')
label2.pack()

text = tk.Text(window,width = 1000,height = 1,bg='#323232',foreground='#B4B4B4',highlightbackground='#323232',font=12)
text.insert(1.0,colorF)
text.pack(padx = 60,pady=10)

palettePhoto2 = ImageTk.PhotoImage(palettePic2)
label3 = tk.Label(window,image = palettePhoto2,bg='#323232')
label3.pack()

text = tk.Text(window,width = 1000,height = 1,bg='#323232',foreground='#B4B4B4',highlightbackground='#323232',font=12)
text.insert(1.0,colorF2)
text.pack(padx = 60,pady=10)

center_window(window, 1000, h+200)
window.mainloop()
# UI呈现
