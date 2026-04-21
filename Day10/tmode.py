try:
	f=open("file1.txt","tw")
	f.write("This is a new file created using t mode")
	f.close()
except FileExistsError:
	print("File already exists")