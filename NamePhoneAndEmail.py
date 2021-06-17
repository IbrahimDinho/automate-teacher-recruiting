# Program to Get name, phone and email from the CV's which are PDFs.

import PyPDF2, os, re, csv

def getPhone(text):
	#America and Canada Numbers
	phoneRegexUSA = re.compile(r'''(
		(\d{3} | \(\d{3}\))?    # Area code
		(\s|-|\.)?		# Seperator
		(\d{3})			# First three digits
		(\s|-|\.)		# Seperator
		(\d{4})			# Last four digits
		)''', re.VERBOSE)
	# UK phone number
	phoneRegexUK = re.compile(r'''(
		07\d{8,12}|447\d{7,11}
		)''', re.VERBOSE)
	matches = []
	for groups in phoneRegexUSA.findall(text):
		matches.append(groups[0])
	for groups in phoneRegexUK.findall(text):
		matches.append(groups[0])
	if len(matches) == 1:
		phoneNumbers = matches[0]
	elif len(matches) < 1:
		phoneNumbers = "No Number registered"
	else : 
		phoneNumbers = "||".join(matches)
	return phoneNumbers

def getEmail(text):
	emailRegex = re.compile(r'''(
		[a-zA-Z0-9._%+-]+  # username 
		@		   # @ symbol
		[a-zA-Z0-9.-]+	   # domain name e.g yahoo
		(\.[a-zA-Z]{2,5})  #.com
		(\.[a-zA-Z]{0,3}) #optional if for example .co.uk
		)''', re.VERBOSE)
	# some cvs have multiple emails 
	matches = []
	for groups in emailRegex.findall(text):
		matches.append(groups[0])
	if len(matches) > 1:
		emails = "|*|".join(matches) # every email seperated by |*| in string.
		return emails
	elif len(matches) < 1 :
		return "No Email"
	else :
		return matches[0]

# change to Directory which holds the CV PDFs
folderToExtract = input("Give me the folder name to get name, phone and email, --make sure you are in correct directory one level above folder which needs extracting \n" )

os.chdir(folderToExtract)

with open('namePhoneEmail.csv', 'w') as new_file:
		fieldnames = ['first_name', 'last_name', 'email', 'phone']
		csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',')
		csv_writer.writeheader()
		new_file.close()
for f in os.listdir('.'):
	file_name, file_ext = os.path.splitext(f)
	Names = file_name.split("_")
	Fname = Names[0]
	# Take into account last Names of variable lengths e.g Alexander Smith Rowe
	Lname = Names[1:]
	Lname = " ".join(Lname)
	
	pdfFileObj = open(f, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	
	# Look at first page as later pages have numbers and emails of references
	pageObj = pdfReader.getPage(0)
	text = pageObj.extractText()
	#print(text) make sure pdf reads text correctly.
		
	phoneNums = getPhone(text)
	emails = getEmail(text)
	# put in CSV file. with name phone and email as coloumns
	with open('namePhoneEmail.csv', 'a') as exist_file:
		fieldnames = ['first_name', 'last_name', 'email', 'phone']
		csv_writer = csv.DictWriter(exist_file, fieldnames=fieldnames)
		csv_writer.writerow({'first_name': Fname, 'last_name': Lname, 'email': emails, 'phone' : phoneNums })
		
	

	pdfFileObj.close()
