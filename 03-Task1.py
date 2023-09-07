"""
Write a Python program to test wether a passed letter is a vowel or not
"""
vowel_list = ['a','e','i','o','u']
found = False
while(1):
    character = input("Please Enter a character : ")
    for i in vowel_list:
        if(character == i):
            found = True
            break
        else:
            found = False
    if(found):
         print("The Enterd Character was Vowel")   
    elif(found==0):
        print("The Enterd Character was not Vowel")

    again = input("Want to enter again press y ")
    if(again == 'y'):
        continue
    else:
        print("Terminating the Program")
        break
    