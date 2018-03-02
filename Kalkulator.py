#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jakub
#
# Created:     16-01-2018
# Copyright:   (c) Jakub 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
print("Witaj w najprostszym możliwym napisanym przeze mnie kalkulatorze. Możesz dodawać, odejmować mnożyć i dzielić")
def add(a,b):
    c = a+b
    print(c)

def substract(a,b):
    c = a-b
    print(c)

def multiply(a,b):
    c = a*b
    print(c)
def division(a,b):
    c = a/b
    print(c)


print("Wpisz pierwszą cyfrę")
a = int(input())
print("Wpisz drugą cyfrę")
b = int(input())
print("Jakie działanie chcesz wykonać? Wybierz: +, -, *, /")

dzialanie = input("Enter operator: ")
if dzialanie == "+":
    add(a,b)
if dzialanie == "-":
    substract(a,b)
if dzialanie == "*":
    multiply(a,b)
if dzialanie == "/":
    division(a,b)