try:
	f=open("file1(x).txt","x")
	f.write("This is a new file created using x mode")
	f.close()
except FileExistsError:
	print("File already exists")