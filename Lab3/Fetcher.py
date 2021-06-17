# Importing libraries
import imaplib, email, base64, datetime

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

imap_url = 'imap.gmail.com'

# Function to get email content part i.e its body part
def get_body(msg):
	if msg.is_multipart():
		return get_body(msg.get_payload(0))
	else:
		return msg.get_payload(None, True)

# Function to search for a key value pair
def search(key, value, con):
	result, data = con.search(None, key, '"{}"'.format(value))
	return data



# Function to get the list of emails under this label
def get_emails(result_bytes):
	con = imaplib.IMAP4_SSL(imap_url, 993)
	con.login(EMAIL_ADDRESS, EMAIL_PASSWD)
	con.select("INBOX")
	msgs = [] # all the email data are pushed inside an array
	for num in result_bytes[0].split():
		typ, data = con.fetch(num, '(RFC822)')
		msgs.append(data)

	return msgs

def fetch():
	# this is done to make SSL connnection with GMAIL
	con = imaplib.IMAP4_SSL(imap_url, 993)

	# logging the user in
	con.login(EMAIL_ADDRESS, EMAIL_PASSWD)

	# calling function to check for email under this label
	con.select('Inbox')

	# fetching emails from this user 
	result, data = con.uid('search', None, "ALL") # (ALL/UNSEEN)
	i = len(data[0].split())

	for x in range(i):
		latest_email_uid = data[0].split()[x]
		result, email_data = con.uid('fetch', latest_email_uid, '(RFC822)')
		# result, email_data = conn.store(num,'-FLAGS','\\Seen') 
		# this might work to set flag to seen, if it doesn't already
		raw_email = email_data[0][1]
		raw_email_string = raw_email.decode('utf-8')
		email_message = email.message_from_string(raw_email_string)

		# Header Details
		date_tuple = email.utils.parsedate_tz(email_message['Date'])
		if date_tuple:
			local_date = datetime.datetime.fromtimestamp(email.utils.mktime_tz(date_tuple))
			local_message_date = "%s" %(str(local_date.strftime("%a, %d %b %Y %H:%M:%S")))
		email_from = str(email.header.make_header(email.header.decode_header(email_message['From'])))
		email_to = str(email.header.make_header(email.header.decode_header(email_message['To'])))
		subject = str(email.header.make_header(email.header.decode_header(email_message['Subject'])))

		# Body details
		for part in email_message.walk():
			if part.get_content_type() == "text/plain":
				body = part.get_payload(decode=True)
				file_name = "email_" + str(x) + ".txt"
				output_file = open(file_name, 'w')
				output_file.write("From: %s\nTo: %s\nDate: %s\nSubject: %s\n\nBody: \n\n%s" %(email_from, email_to,local_message_date, subject, body.decode('utf-8')))
				output_file.close()
			else:
				continue
