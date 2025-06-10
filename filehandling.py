# file handling 
with open("file1.txt","r+") as myfile:       # r+ mode opens the file for both read and write
    print(myfile.read())
    myfile.write("I am fine")
myfile.close()

"""
output:
running it first time in terminal :
Hello,how are you?

now file1.txt it will contain :
Hello,how are you?
I am fine

running it second time in terminal :
Hello,how are you?
I am fine

# now file1.txt it will contain :
Hello,how are you?
I am fineI am fine
"""

