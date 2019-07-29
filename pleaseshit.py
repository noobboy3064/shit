repeat_count = True
from math import *

#function
def subtraction():
    num3 = 0
    num2 = 0
    num1 = 0
    num1 = input("please enter your number")
    num2 = input("please enter your second number")
    try:
        num3 = float(num1) - float(num2)
        if num3 == 80085:
            print("dirty *******")
        else:
            print(num3)
    except:
           print("you fu******* **** ******** **** **** and have no ***** **** thing to do right?")
    print("press any key to continue")

def multiplication():
    num3 = 0
    num2 = 0
    num1 = 0
    num1 = input("please enter your number")
    num2 = input("please enter your second number")
    try:
        num3 = float(num1) * float(num2)
        if num3 == 80085:
            print("dirty *******")
        else:
            print(num3)
    except:
           print("you fu******* **** ******** **** **** and have no ***** **** thing to do right?")
    print("press any key to continue")

def division():
    num3 = 0
    num2 = 0
    num1 = 0
    num1 = input("please enter your number")
    num2 = input("please enter your second number")
    try:
        num3 = float(num1) / float(num2)
        if num3 == 80085:
            print("dirty *******")
        else:
            print(num3)
    except:
           print("you fu******* **** ******** **** **** and have no ***** **** thing to do right?")
    print("press any key to continue")


def addition():
    num3 = 0
    num2 = 0
    num1 = 0
    num1 = input("please enter your number: ")
    num2 = input("please input your second number: ")
    try:
        num3 = float(num1) + float(num2)
        if num3 == 80085:
            print("dirty *******")
        else:
            print(num3)
    except:
        print("you fu******* **** ******** **** **** and have no ***** **** thing to do right?")
    print("press any key to continue")

while repeat_count == True:
    print('please enter your operator')
    operator = input("enter here")
    if operator == "addition":
     addition()


    elif operator == "subtraction":
     subtraction()


    elif operator == "multiplication":
     multiplication()


    elif operator == "division":
     division()


    else:
     print("invalid operator")

     print("do you want to continue?")
     repeat = input('')


    repeat = input('')

    if repeat == 'no':
     repeat_count = False
    else:
         print("processing. please wait")


