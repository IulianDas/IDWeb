import tkinter as tk
from tkinter.constants import INSERT
from PIL import ImageTk,Image
import socket,threading,sys,time
class EntryWithPlaceholder(tk.Entry):
	def __init__(self,master=None,placeholder='PLACEHOLDER',color='red'):super().__init__(master);self.placeholder=placeholder;self.placeholder_color=color;self.default_fg_color=self['fg'];self.bind('<FocusIn>',self.foc_in);self.bind('<FocusOut>',self.foc_out);self.put_placeholder()
	def put_placeholder(self):self.insert(0,self.placeholder);self['fg']=self.placeholder_color
	def foc_in(self,*args):
		if self['fg']==self.placeholder_color:self.delete('0','end');self['fg']=self.default_fg_color
	def foc_out(self,*args):
		if not self.get():self.put_placeholder()
sucket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
log=[]
def sendMsg():global log;message=getMessage();sucket.send(bytes(message,'utf-8'));hackOfTheCentury=bytes(message,'utf-8');hackOfTheCentury=str(hackOfTheCentury,'utf-8');log.append(hackOfTheCentury)
def refresh():
	global log;data=sucket.recv(1024)
	if not data:sys.exit()
	data=str(data,'utf-8');print(log)
	for iten in range(len(log)):
		print(log[iten])
		if log[iten]in data:data=data.replace(log[iten],'')
	textBox.insert(INSERT,data+'\n')
def initClient(address):sucket.connect((address,10000))
def callback():root.quit()
def connect(route):client=initClient(route)
def onConnectClick():route=str(routeEntry.get());connect(route)
def getMessage():message=None;message=str(msgEntry.get());msgEntry.delete(0,'end');return message
root=tk.Tk()
root.title('Chat client for laborator 5')
root.protocol('WM_DELETE_WINDOW',callback)
routeFrame=tk.LabelFrame(root,text='Route',padx=5,pady=5,font=('Cascadia Code PL',10,'bold'))
routeFrame.grid(row=1,column=0,rowspan=2)
routeLabel=tk.Label(routeFrame,text='Server adress : ',font=('Cascadia Code PL',10,'bold'))
routeLabel.grid(row=2,column=0)
routeEntry=EntryWithPlaceholder(routeFrame,'192.168.0.10')
routeEntry.grid(row=3,column=0)
routeBtn=tk.Button(root,text='Connect',font=('Cascadia Code PL',10,'bold'),command=onConnectClick,width=25)
routeBtn.grid(row=1,column=1)
msgFrame=tk.LabelFrame(root,text='Message',padx=5,pady=5,font=('Cascadia Code PL',10,'bold'))
msgFrame.grid(row=4,column=0,columnspan=3)
msgLabel=tk.Label(msgFrame,text='Your message : ',font=('Cascadia Code PL',10,'bold'))
msgLabel.grid(row=5,column=0,columnspan=3)
msgEntry=tk.Entry(msgFrame,width=55)
msgEntry.grid(row=6,column=0,columnspan=3)
msgBtn=tk.Button(root,text='Send',font=('Cascadia Code PL',10,'bold'),command=sendMsg,width=25)
msgBtn.grid(row=2,column=1)
refreshBtn=tk.Button(root,text='Refresh',font=('Cascadia Code PL',10,'bold'),command=refresh,width=45)
refreshBtn.grid(row=6,column=0,columnspan=2)
textBox=tk.Text(root,width=45)
textBox.grid(row=7,column=0,columnspan=3)
root.mainloop()
