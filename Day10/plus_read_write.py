try:
	f=open("demo2.txt","r+")
	content=f.read()
	f.write("\nThis is a line added using r+ mode")
	print(content)
	f.seek(0)
	content2=f.read()
	print(content2)
	f.close()
except Exception as e:
	print("An error occurred:", e)

try:
	f=open("demo3.txt","w+")
	f.write("This is a line added using w+ mode")
	f.seek(0)
	content=f.read()
	print(content)
	f.close()
except Exception as e:
	print("An error occurred:", e)

try:
	f=open("demo4.txt","a+")
	f.write("This is a line added using a+ mode")
	f.seek(0)
	content=f.read()
	print(content)
	f.close()
except Exception as e:
	print("An error occurred:", e)

