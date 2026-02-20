#Q1
'''
import math_util as calc

calc.add(2, 3)
calc.sub(8, 3)
calc.mul(2, 3)
calc.div(6, 3)
'''

#Q2
'''
import math as m

print(f"Square root of 49 is : {m.sqrt(49)}")
print(f"sin(90) = {m.radians(90)} radians")
'''

#Q3
'''
import srting_util as s

string = input("Enter any string: ")
s.vowels(string)
'''

#Q4
'''
from srting_util import greet as g

name = input("Enter your name: ")
g(name)
'''

#Q5
'''
import helper
#This function can't run in main file.
'''

#Q6
'''
from shaps import circle as c, rectangle as r

length = int(input("Enter length of rectangle: "))
width = int(input("Enter width of rectangle: "))

r.perimeter(length, width)
r.area(length, width)

radius = int(input("\nEnter radius of circle: "))

c.circumference(radius)
c.area(radius)
'''

#Q7
'''
from utilies import file_utils as f, date_utils as d

f.file_handling("sample.txt", "\nLearning packeges...")

d1 = input("Enter first date(YYYY-MM-DD): ")
d2 = input("Enter second date(YYYY-MM-DD): ")

d.days(d1, d2)
'''

#Q8
'''
import math as m

print("Methods and attributes of math class:")
print(dir(m))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name of person is {self.name} and age {self.age}")

p = Person("Rensee", 21)

print("\nMethods and Attributes of custom class:")
print(dir(p))
'''

#Q9
'''
from geometry import c_area, t_area, circumference

circumference(2)
c_area(2)
t_area(10, 5)
'''