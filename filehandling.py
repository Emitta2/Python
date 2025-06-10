"""
with open("file1.txt","r+") as myfile:       # r+ mode opens the file for both read and write
    print(myfile.read())
    myfile.write("I am fine")
myfile.close()
"""
"""
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

# random.randint is used to generate random integer in the given range in which both the range are inclusive
"""
import random
print(random.randint(1,5))      # generates a random integer between 1 and 5 (both inclusive)
"""
# random.randrange is used to generate random integer in the given range in which the first range is inclusive and the second range is exclusive
"""
import random
print(random.randrange(1,5))    # generates a random integer between 1 and 5 (1 inclusive, 5 exclusive)

print(random.randrange(1,10,2)) # generates a random integer between 1 and 10 (1 inclusive, 10 exclusive) with a step of 2 eg:13579(odd no)
print(random.randrange(2,11,2)) # generates a random integer between 2 and 11 (2 inclusive, 11 exclusive) with a step of 2 eg:246810 (even no)
print(random.choice([1,2,3,4])) # generates random no from a given list eg. 1,2,3,4
 mylist=[11,45,6,89]
print(random.choice(mylist))    # generates from mylist eg. 11,45,6,89
"""
# random.random() will generate decimalno. from 0 to 1 (0.0 inclusive, 1.0 exclusive)
import random

