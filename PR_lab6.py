from tkinter import *
import time,datetime
from socket import *
import threading,pyautogui
from PIL import ImageTk,Image,ImageFile
import numpy as np,cv2
ImageFile.LOAD_TRUNCATED_IMAGES=True
def get_host():host=entry1.get();return host
def screenshot(filename):myScreenshot=pyautogui.screenshot();myScreenshot.save(filename)
def run():
	current_time=str(datetime.datetime.now());current_time=current_time.replace(' ','').replace(':','-');file_name='{}.png'.format(current_time);screenshot(file_name);s=socket(AF_INET,SOCK_DGRAM);host=get_host();host=host.encode();port=9999;buf=1024;addr=host,port;file_name=file_name.encode();s.sendto(file_name,addr);f=open(file_name,'rb');data=f.read(buf)
	while data:
		if s.sendto(data,addr):data=f.read(buf)
	s.close();f.close();print(f"{file_name}.png sent o7");time.sleep(8)
def run_run():
	while True:run()
def show_img(filename):img=cv2.imread(filename);imS=cv2.resize(img,(960,540));cv2.imshow('image',imS);cv2.waitKey(3000);cv2.destroyAllWindows()
def get():
	host='0.0.0.0';port=9999;s=socket(AF_INET,SOCK_DGRAM);s.bind((host,port));addr=host,port;buf=1024;data,addr=s.recvfrom(buf);print('Fisier receptionat:',data.strip());f=open(data.strip(),'wb');filename=data.strip().decode();data,addr=s.recvfrom(buf)
	try:
		while data:f.write(data);s.settimeout(2);data,addr=s.recvfrom(buf)
	except timeout:f.close();s.close();a_thread=threading.Thread(target=show_img(filename));a_thread.start();print('Fisierul downloaded')
def get_get():
	while True:get()
def callback():root.quit()
root=Tk()
root.title('UDP 6')
root.protocol('WM_DELETE_WINDOW',callback)
entry1=Entry(root,width=25)
entry1.pack()
button2=Button(root,text='Trimite',command=lambda:threading.Thread(target=run_run).start(),font='Arial',width=20)
button2.pack()
button1=Button(root,text='Primeste',command=lambda:threading.Thread(target=get_get).start(),font='Arial',width=20)
button1.pack()
root.mainloop()
