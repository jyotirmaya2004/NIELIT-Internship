import os
if os.path.exists("hello3.txt"):
	print("The file exists.")
	os.remove("hello3.txt")  # Delete the file
	print("File deleted successfully.")
else:
	print("The file does not exist.")