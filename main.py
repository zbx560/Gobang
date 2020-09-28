#!/usr/bin/env python
#-*- coding: utf-8 -*-

import GUI
import tkinter
import pygame
import tkinter.filedialog


if __name__ == '__main__':
    # 初始化
    pygame.mixer.init()
    #文件加载
    a = tkinter.filedialog.askopenfilename() or '.\FromTheNewWorld.mp3'
    pygame.mixer.music.load(a)
    # 播放  第一个是播放值 -1代表循环播放， 第二个参数代表开始播放的时间
    pygame.mixer.music.play(-1, 10)

    window = tkinter.Tk()
    gui_chess_board = GUI.Chess_Board_Frame(window)
    gui_chess_board.pack()
    window.mainloop()

