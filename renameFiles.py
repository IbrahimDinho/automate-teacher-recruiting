#Rename a folder with lots of CV files in a format of firstName_LastName.pdf from previous format Anik_Marchand-d0dd5e7b.pdf 
import os


folderToRename = input("Give me the folder name to organise, --make sure you are in correct directory one level above folder which needs organising \n" )

currentDir = os.getcwd()
try:
# instead of input can also hardcode it so replace folderToRename to hardcode
	os.chdir(currentDir + "/" + folderToRename);
except FileNotFoundError:
	print("Folder does not exist, check spelling and its in correct directory")
	exit();

for f in os.listdir('.'):
	file_name, file_ext = os.path.splitext(f)
	if "-" not in file_name:
		print("This file is different (no - or has been formatted already)" + file_name);
	else:
		nameArray = file_name.split("-")
		fName = nameArray[0]
		file_ext = file_ext.strip()
		fName = fName.strip()

# capitalise first and last name first letter.
		l = list(fName.lower())
		index = 0
		for i in range(len(l)):
			if l[i] == '_':
				index = i + 1
				break
		if index != 0:
			l[index] = l[index].upper()
		l[0] = l[0].upper()
		fName = ''.join(l)

			
			
				
		newName = f"{fName}{file_ext}"
		os.rename(f, newName)

print("Name of files have been formatted in folder using format e.g Ibrahim_Elma.pdf")


