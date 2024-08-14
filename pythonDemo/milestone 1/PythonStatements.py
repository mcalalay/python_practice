hungry = False
if (hungry):
    print("Feed me!")
else:
    print("I'm not hungry")

loc = "Auto Shop"
if loc == "Auto Shop":
    print("I have a jimny man")
elif loc == "Bank":
    print("Get your emergency savings now")
else:
    print("ediwow")

Greetings = "Hi, I'm Matthew. How is your day?"
numbers = [1,2,3,4,5,6,78,8]
for i in numbers:

    if i % 2 ==0:
        print(i)
    else:
        print(f"Odd Number: {i}")

list_sum =0
for i in numbers:
    list_sum = list_sum + i
print(list_sum)

for char in Greetings:
    print(char)

x=0
while x<10:

    x += 2
    print(f"The current value of x is {x}")

else:
    print(f"X is no longer less than 10, it is {x}")

mylist= [1, 2,3]
for num in range(3,10,3):
    print(num)


mystring= "Hello"
mylist = [letter for letter in mystring]
print(mylist)

myNewList = [ x for x in "This is the input to be converted into a list"]
print(myNewList)

myEvenNumberList = [ x*10 for x in range(0,100) if x%2==0]
print(myEvenNumberList)

myNewListOfNumbers = []
for x in [2,4,6]:
    for y in [100,200,300]:
        myNewListOfNumbers.append(x*y)
print(myNewListOfNumbers)