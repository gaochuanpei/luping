"""python + opencv 实现屏幕录制"""
from PIL import ImageGrab
import numpy as np
import cv2
import win32gui
import easygui as g
while True:
	title = g.enterbox(msg="需要录制的软件名称，全屏录制请输入'然然'",title="小川来录屏")
	if title:
		if title =="然然":
			p = ImageGrab.grab()#获得当前屏幕
			k=np.zeros((200,200),np.uint8)
			a,b=p.size#获得当前屏幕的大小
		else:
			try:
				hwnd = win32gui.FindWindow(None, title)
				rect = win32gui.GetWindowRect(hwnd)
				a=rect[2]-rect[0]
				b=rect[3]-rect[1]
				k=np.zeros((200,200),np.uint8)
			except:
				g.msgbox(msg="没这个软件，别逗我")
				continue
		FileName = g.enterbox(msg="保存的文件名称",title="小川来录屏")
		while (not FileName):
			FileName = g.enterbox(msg="保存的文件名称",title="小川来录屏")
		fourcc = cv2.VideoWriter_fourcc(*'XVID')#编码格式
		#输出文件帧率为16，可以自己设置
		video = cv2.VideoWriter(FileName+".avi", fourcc, 16, (a,b))
		while True:
			im = ImageGrab.grab(rect)
			imm=cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)#转为opencv的BGR格式
			video.write(imm)
			cv2.imshow('imm',k)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
		video.release()
		cv2.destroyAllWindows()
	else:
		break
