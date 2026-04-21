try:
	f=open("binary.txt","wb")
	f.write(b"This is a binary file")
	f.write(b"This is another line in the binary file")
	f.close()
except Exception as e:
	print("An error occurred:", e)
