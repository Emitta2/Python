# fizzbuzz

def fizzBuzz(r):
    for i in range(1,r):
        if (i%3==0 and i%5==0):
            print(str(i)+" = FizzBuzz")     
        elif (i%3==0):
            print(str(i)+" = Fizz")
        elif (i%5==0):
            print(str(i)+" = Buzz")
        else:
            print(str(i))
fizzBuzz(31)

# without function
for i in range(1,51):
        if (i%3==0 and i%5==0):
            print(str(i)+" = FizzBuzz")
        elif (i%3==0):
            print(str(i)+" = Fizz")
        elif (i%5==0):
            print(str(i)+" = Buzz")
        else:
            print(str(i))

"""
sample output:
1
2
3 = Fizz
4
5 = Buzz
6 = Fizz
7
8
9 = Fizz
10 = Buzz
11
12 = Fizz
13
14
15 = FizzBuzz
...
"""