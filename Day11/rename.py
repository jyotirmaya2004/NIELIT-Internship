import os
if os.path.exists("hello2.txt"):
	print("The file exists.")
	os.rename("hello2.txt", "renamed_file.txt")  # Rename the file
	print("File renamed successfully.")
else:
	print("The file does not exist.")