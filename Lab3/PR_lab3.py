import smtplib
import base64
from email.message import EmailMessage
import imghdr
from tkinter import *
from fetcher import *
import os
import os.path

root = Tk()
root.title("Laborator 3")


def base64_decode(string):
	base64_bytes = string.encode('ascii')
	message_bytes = base64.b64decode(base64_bytes)
	message = message_bytes.decode('ascii')
	return message

def custom_b64d(string):
	return base64_decode(string)

EMAIL_ADDRESS = 'YmVzdGVtYWlsZm9ydGVzdEBnbWFpbC5jb20='
EMAIL_PASSWD = 'U2FuYzN6MDY4NTM0MDkz'

EMAIL_ADDRESS = custom_b64d(EMAIL_ADDRESS)
EMAIL_PASSWD = custom_b64d(EMAIL_PASSWD)


def set_msg(msgSubj, msgTo, msgContent):
	msg = EmailMessage()
	msg['Subject'] = msgSubj
	msg['From'] = EMAIL_ADDRESS
	msg['To'] = msgTo
	msg.set_content(msgContent)


	return msg


def send_msg(msg):
	with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
		smtp.login(EMAIL_ADDRESS, EMAIL_PASSWD)
		smtp.send_message(msg)


def onClick():
	msgSubj = msgSubjEntry.get()
	msgTo = msgToEntry.get()
	msgContent = msgEntry.get()
#	print(msgSubj, msgTo, msgContent)
	msg = set_msg(msgSubj, msgTo, msgContent)
	send_msg(msg)

def count_emails():
	emails = []
	emails.append(([f for f in os.listdir('.') 
     if f.endswith('.txt') and os.path.isfile(os.path.join('.', f))]))
#	print(emails)
	return emails
#	for i in range(len(emails)):
#		print(emails[i])

def flatten_list(_2d_list):
    flat_list = []
    # Iterate through the outer list
    for element in _2d_list:
        if type(element) is list:
            # If the element is of type list, iterate through the sublist
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list

def otherOnClick():
	# frum = msgFromEntry.get().replace(" ", "")
	fetch()
	emails = count_emails()
#	print(emails)
	emails = flatten_list(emails)
#	print(emails)

	for i in range(len(emails)):
		with open(emails[i], 'r') as f:
			textbox.insert(INSERT, f.read())


# First frame for all the things
sendFrame = LabelFrame(root, text="Transmite un mesaj", padx=5, pady=5, font=("arial", 10, "bold"))
sendFrame.grid(row=1, column=0, columnspan=3)
# Text above the subject entry
# msgFromLabel = Label(sendFrame, text="Enter your from : ", font=("arial", 10, "bold")) 
# msgFromLabel.grid(row=2, column=0)
# Entry for the From
# msgFromEntry = Entry(sendFrame, width=50)
# msgFromEntry.grid(row=3, column=0)
# Text above the from entry
msgSubjLabel = Label(sendFrame, text="Tema mesajului: ", font=("arial", 10, "bold")) 
msgSubjLabel.grid(row=4, column=0)
# Entry for the Subj
msgSubjEntry = Entry(sendFrame, width=50)
msgSubjEntry.grid(row=5, column=0)
# Text above the to entry
msgToLabel = Label(sendFrame, text="Adresa destinatarului: ", font=("arial", 10, "bold")) 
msgToLabel.grid(row=6, column=0)
# Entry for the to
msgToEntry = Entry(sendFrame, width=50)
msgToEntry.grid(row=7, column=0)
# Text above the message entry
msgLabel = Label(sendFrame, text="Introduce-ti mesajul: ", font=("arial", 10, "bold")) 
msgLabel.grid(row=8, column=0)
# Entry for the message
msgEntry = Entry(sendFrame, width=50)
msgEntry.grid(row=9, column=0)
# Button for sending the message
SendButton = Button(sendFrame, text="Transmite", font=("arial", 10, "bold"), command=onClick)
SendButton.grid(row=10, column=0)
# Second frame for all the things
fetchFrmae = LabelFrame(root, text="Afiseaza mesajele", padx=5, pady=5, font=("arial", 10, "bold"))
fetchFrmae.grid(row=11, column=0, columnspan=3)
# Text above the from entry
#msgFromLabel = Label(fetchFrmae, text="Enter your sender email : ", font=("arial", 10, "bold")) 
#msgFromLabel.grid(row=12, column=0)
# Entry for the from
# msgFromEntry = Entry(fetchFrmae, width=50)
# msgFromEntry.grid(row=13, column=0)
# Button for fetching the message
SendButton = Button(fetchFrmae, text="Afiseaza", font=("arial", 10, "bold"), command=otherOnClick)
SendButton.grid(row=14, column=0, columnspan=3)
textbox = Text(fetchFrmae)
textbox.grid(row=15, column=0, columnspan=3)

root.mainloop()
