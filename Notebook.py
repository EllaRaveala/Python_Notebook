import time
import pickle

file= "notebook.dat"
list=[]

try:
	filename=open(file,"wb")
	filename.close()

except Exception:
	print("No default notebook was found, created one.")
	
filename=open(file,"wb")
pickle.dump(list,filename)

filename=open(file,"rb")
fileread = pickle.load(filename)

while True:	
	print("(1) Read the notebook")
	print("(2) Add note")
	print("(3) Edit a note")
	print("(4) Delete a note")
	print("(5) Save and Quit")

	choice=int(input("Please select one: "))
	
	if choice==1:		
		for i in range(0, len(fileread)):
			print(fileread[i])
		
	elif choice==2:
		note= input("Write a new note: ")
		datetime= time.strftime("%X %x")
		string= note + ":::" + str(datetime)

		fileread.append(string)

	elif choice==3:
		print("The list has", len(fileread), "notes.")
		index=int(input("Which of them will be changed?:"))
		print(fileread[index])
		fileread.pop(index)
		
		newnote= input("Give the new note: ")
		datetime= time.strftime("%X %x")
		string= newnote + ":::" + str(datetime)
		fileread.insert(index, string)

	elif choice==4:
		print("The list has", len(fileread), "notes.")
		index=int(input("Which of them will be deleted?:"))
		try:
			print("Deleted note", fileread[index])
			fileread.pop(index)
		except IndexError:
			print("Deleted note", fileread[index-1])
			fileread.pop(index-1)

	elif choice==5:
		print("Notebook shutting down, thank you.")
		filename.close()
		break
	else:
		print("Incorrect selection")
