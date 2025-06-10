# random library
import random

# random.randint is used to generate random integer in the given range in which both the range are inclusive
print(random.randint(1,5))      # generates a random integer between 1 and 5 (both inclusive)

# random.randrange is used to generate random integer in the given range in which the first range is inclusive and the second range is exclusive
print(random.randrange(1,5))    # generates a random integer between 1 and 5 (1 inclusive, 5 exclusive)
print(random.randrange(1,10,2)) # generates a random integer between 1 and 10 (1 inclusive, 10 exclusive) with a step of 2 eg:13579(odd no)
print(random.randrange(2,11,2)) # generates a random integer between 2 and 11 (2 inclusive, 11 exclusive) with a step of 2 eg:246810 (even no)
print(random.choice([1,2,3,4])) # generates random no from a given list eg. 1,2,3,4
mylist=[11,45,6,89]
print(random.choice(mylist))    # generates from mylist eg. 11,45,6,89

# random.random() will generate random decimalno. from 0 to 1 (0.0 inclusive, 1.0 exclusive)
print(random.random())