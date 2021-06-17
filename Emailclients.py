#Read csv email coloumn and send out bulk emails

#open and read csv email data
import csv, smtplib, os
from email.message import EmailMessage



with open('TestRegex/namePhoneEmail.csv', newline ='') as csvfile:
	reader = csv.DictReader(csvfile)
	emailList = set() #set so no duplicates to resend email twice to same person
	for row in reader:
		emailList.add(row['email'])
	
		
# Get username and password in secure way using environment variables.
EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')


msg = EmailMessage()
msg['Subject'] = 'English Teaching application'
msg['From'] = 'ibrahimelmagbari7@gmail.com'
msg['To'] = 'ibbyi7i@yahoo.com'
contacts = list(emailList)
msg['Bcc'] = contacts
content = input("what is the message you want to send \n")
msg.set_content(content)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
	smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
	smtp.send_message(msg)
	print("Emails sent")
	

