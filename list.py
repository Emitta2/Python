# List
shopping=["Bread","Coffee","Sugar"]
print(shopping)                       # ['Bread', 'Coffee', 'Sugar']

# To display items one below the other
for item in shopping:    # here item is an intuitive name,you can give any name like i
    print(item)            # but same name should be given in the print stmt
print(shopping)
"""  Bread
     Coffee
     Sugar   """

## MANIPULATION 
# append   To add an item to the list
shopping.append("Curd")
print(shopping)                    # ['Bread', 'Coffee', 'Sugar', 'Curd']

#indexing  To access items in the list
print(shopping[0])  # Bread
print(shopping[1])  # Coffee

# to print items of a list one after the other
for i in range(4):            
    print(shopping[i])
""" Bread
    Coffee
    Sugar
    Curd  """
for item in shopping:   # alternative way to print items,same output
    print(item)

shopping.append("Shampoo")
print(shopping)            # ['Bread', 'Coffee', 'Sugar', 'Curd', 'Shampoo']

# To insert an item at a specific position
shopping.insert(1,"Oil")
print(shopping)            # ['Bread', 'Oil', 'Coffee', 'Sugar', 'Curd', 'Shampoo']

# count   To count the number of occurrences of an item in the list
ages=[12,23,34,42,15,87,12,16,25,23,82,57,7,3,2,3,1,20]
print(ages.count(25)) # 1
print(ages.count(12)) # 2
print(ages.count(70)) # 0

# len To find the length of the list
print(len(ages)) # 18
print(len(shopping))  # 6

for i in range(len(shopping)):
    print(shopping[i])
""" Bread
    Oil
    Coffee
    Sugar
    Curd
    Shampoo """
# alternative way without range
for item in shopping:
    print(item)

## OPERATIONS
# count
ages=[12,23,34,42,15,87,12,16,25,23,82,57,7,3,2,3,1,20]
print(ages.count(25)) # 1

# sort
ages.sort()  # sorts the list in ascending order
print(ages)  # [1, 2, 3, 3, 7, 12, 12, 15, 16, 20, 23, 23, 25, 34, 42, 57, 82, 87]

students=["Arun","Rajesh","Harish","Akansha","Lakshmi","Varsha"]
students.sort()  # sorts the list of students in alphabetical order
print(students)  # ['Akansha', 'Arun', 'Harish', 'Lakshmi', 'Rajesh', 'Varsha']

students.insert(0,"JOC")
print(students)        # ['JOC', 'Akansha', 'Arun', 'Harish', 'Lakshmi', 'Rajesh', 'Varsha']

# reverse
ages.reverse()  # reverses the order of the list
print(ages)  # [87, 82, 57, 42, 34, 25, 23, 23, 20, 16, 15, 12, 12, 7, 3, 3, 2, 1]

## SLICING
#list_name[startindex:endindex+1]
print(students[1:5])  # ['Akansha', 'Arun', 'Harish', 'Lakshmi'] starts with index 1 and ends with index 5-1=4
print(students[:])  # entire list ['JOC', 'Akansha', 'Arun', 'Harish', 'Lakshmi', 'Rajesh', 'Varsha'] starts from index 0 to end
print(students[3:])  # ['Harish', 'Lakshmi', 'Rajesh', 'Varsha'] starts from index 3 to end
print(students[:5]) # ['JOC', 'Akansha', 'Arun', 'Harish', 'Lakshmi'] starts from index 0 to index 5-1=4
# default start index is 0 and default end index is len(list)
print(students[2:5]) # ['Arun', 'Harish', 'Lakshmi'] starts from index 2 to index 5-1=4

