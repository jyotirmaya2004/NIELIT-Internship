try:
	with open("demo.txt", "r") as f:
		position = f.tell()  # Get the current position of the file pointer
		print("Current position:", position)
		content = f.read()
		print(content)
		position = f.tell()  # Get the current position of the file pointer
		print("Current position:", position)
		position=f.seek(0)  # Move the file pointer back to the beginning of the file
		print("After seek(0):",position)

		f.seek(5)  # Move the file pointer to the 5th byte
		print("After seek(5):",f.tell())
		f.seek(+10)  # Move the file pointer 10 bytes forward from the current position
		print("After seek(+10):",f.tell())
		f.seek(-5,1)  # Move the file pointer 5 bytes backward from the current position
		print("After seek(-5,1):",f.tell())
		f.seek(-10,2)  # Move the file pointer 10 bytes backward from the end of the file
		print("After seek(-10,2):",f.tell())
		f.seek(0,2)  # Move the file pointer to the end of the file
		print("After seek(0,2):",f.tell())

		#f.seek () syntax: f.seek(offset, whence)
		#offset: The number of bytes to move the file pointer.
		#whence: The reference point for the offset (0 for beginning, 1 for current position, 2 for end of file).


except Exception as e:
	print("An error occurred:", e)