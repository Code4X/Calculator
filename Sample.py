#String Manupulation

print("5" + "5");
print("This costs " + str(6) + " dollars");
print("This costs " + str(5+7) + " dollars");
print("Hello:Nick".split(":"));
print("Hello:Nick:World".split(":"));
print("My name is " + "Kalp:Hello:World".split(":")[0]);
print("There are " + "24:16:4".split(":")[0] + " hours in a day");

#Boolean Operators

print()
print(5==5)
print(5==4)
print(5 is not 5)
print(5 is 5)
print("this" is "this")
print("True" is str(True))

#Lists

print()
print(["Movies", "Games", "Python"])
print("I love coding with " + ["Movies", "Games", "Python"][2] + ".")
print("I love " + ["Movies", "16", "Python"][1]);

#Dictionaries

print()
print({"name": "Kalp", "age": "18", "hobby": "Coding"})
print("Name is " + {"name": "Kalp", "age": "18", "hobby": "Coding"}['name'])
print("Age is " +{"name": "Kalp", "age": "18", "hobby": "Coding"}['age'])
print("Hobby is " +{"name": "Kalp", "age": "18", "hobby": "Coding"}['hobby'])

#Variables

print()
greeting = "Hello, how are you? "
statement = "I hope you're doing well."
print(greeting + statement)

greeting = greeting.split(",")[0] #split it at comma
print(greeting)

print(greeting + " Kalp")
greeting = greeting + " Kalp"

print(greeting)

num1 = 1
num2 = 2
print(num1*num2 + num2*num1)
check = True

#Built-in Functions

print()
print(str(16))
print(str(True))
print(int("5"))
print(float("5.6"))
print(bool("True")) #convert to boolean
print(len("Hello my name is Kalp")) #length of text/array
print(len([1, 2, 3, 2, 9]))
print(len(["Kalp", "Preet"]))
print(sorted([16, 3, 8, 6, 9, 133, 435, 21, 823, 45])) #puts array in acending order
print(sorted(["Kalp", "Preet", "John", "Lu", "A", "b", "3", "1", "1.534"]))

#User-Defined Functions
print()
def my_function():
    print("This is my function!")
    print("A second string.")
my_function()

#Adding Arguments to a Function

print()
def my_function(str1, str2):
    print(str1)
    print(str2)
my_function("This is argument 1", "I love hockey")
my_function("Hello", "world")

#Default Arguments

print()
def print_something(name = "Someone", age = "Unknown"):
    print("My name is", name, "and my age is", age)
print_something("Kalp", 18)

def print_something(name = "Someone", age = "Unknown"):
    print("My name is", name, "and my age is", age)
print_something()

#Keyword Arguments

print()
def print_something(name = "Someone", age = "Unknown"):
    print("My name is", name, "and my age is", age)
print_something(None, 18)

def print_something(name = "Someone", age = "Unknown"):
    print("My name is", name, "and my age is", age)
print_something(age = 18, name = "Kalp")

#Infinte Arguments

print()
def print_people (*people):
    for person in people:
        print("This person is", person)

print_people("Kalp", "Jack", "King", "Smiley", "Dan")

#Return Values from Functions
print()
def do_math(num1, num2):
    return num1 + num2
math1 = do_math(5, 7)
math2 = do_math(11, 34)

print("First sum is", math1, "and the second sum is", math2)

#Conditional Statements

print()
check = "Hamburger"
if check==False:
    print("It is false")
elif check=="Hamburger":
    print("YUMMM hamburgers")
elif check=="Yo":
    print("Hello")

else:
    print("It is actually equal to True")

#Loops

print()
numbers = [1, 2, 3, 4, 5]
for items in numbers:
    print(items)
words = ["Kalp", "Preet", "Jack", "Lu"]
for lists in words:
    print("This person's name is ",lists)

run = True
current = 1

while run:
    if current==10:
        run=False
    else:
        print(current)
        current += 1

#Importing Libraries

import re
string = "'I AM NOT YELLING', she said. Though we knew it to not be true."

new = re.sub('[A-Z]', '', string) #Removes all capital letters from A-Z
print(new)

new = re.sub('[a-z]', '', string) #Removes all lowecase letters from a-z
print(new)

new = re.sub('[.,\']', '', string) #Removes all special characters
print(new)

new = re.sub('[A-Z+" "]', '', string) #Removes spaces and capital letters
print(new)

string = string + "6 298 - 345"
print(string)

new = re.sub('[^0-9]', '', string)
print(new)

