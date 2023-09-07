"""
Task1 : Write a Python Program to count the number 4 in a given list
"""
list1 = [1, 4, 6, 7, 4]
number = 4
count = 0
for i in list1 :
    if(number == i):
        count+=1
print(f"The Number 4 is found in the list {count} times")