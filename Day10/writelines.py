lines=["Hello World\n", "Welcome to Python\n", "File handling is easy\n", "Have a nice day\n"]
f=open("file2.txt","w")
f.writelines(lines)
f.close()