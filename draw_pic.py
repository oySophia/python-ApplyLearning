# coding=utf-8
#!/usr/bin/python

from Tkinter import *
from FileDialog import *
from PIL import Image

#file_name = 'a.jpg'


def getFileName():
    file_dialog = LoadFileDialog(frame)
    global file_name
    file_name = file_dialog.go()
    try:
        img = Image.open(file_name)
    except:
        print 'openfile error'
    show_img.image = img
    show_img.pack()


def gen():
    try:
        img_o = Image.open(file_name)
    except:
        print 'openfile error'
    img_L = img_o.convert('L')
    size_x, size_y = img_o.size
    size_y = size_y * 80 / size_x / 2
    size_x = 80
    # img_L.resize((size_x, size_y)).show()
    data = list(img_L.resize((size_x, size_y)).getdata())

    min_x, min_y = size_x, size_y
    max_x, max_y = 0, 0

    for i in range(0, size_y):
        for j in range(0, size_x):
            index = i * size_x + j
            if data[index] <= 170:
                min_x, min_y = min(min_x, j), min(min_y, i)
                max_x, max_y = max(max_x, j), max(max_y, i)
    genText.delete('1.0', 'end')
    for i in range(min_y, max_y + 1):
        for j in range(min_x, max_x + 1):
            index = i * size_x + j
            if data[index] > 170:
                to = ' '
            elif data[index] > 85:
                to = '1'
            else:
                to = '0'
            genText.insert('end', to)
        # print
        genText.insert('end', '\n')


if __name__ == "__main__":
    mainWindow = Tk()
    mainWindow.title()
    # mainWindow.geometry('640x480+0+0')

    frame = Frame(mainWindow)
    frame.pack()

    fileBotton = Button(frame, text=u"打开文件", command=getFileName)
    fileBotton.pack(side=LEFT)

    genBotton = Button(frame, text=u"生成", command=gen)
    genBotton.pack(side=LEFT)

    genText = Text(frame, height=40)
    genText.pack(fill=BOTH, padx=10, pady=10)

    show_img = Label(frame)
    show_img.pack()
    mainWindow.mainloop()