st = "Print only the words that start with s in this sentence"
splitSt= st.split()
print(splitSt)
for portion in splitSt:
    if portion[0] == "s":
        print(portion)

for x in range(0,11):
    if x%2==0:
        print(x)

y= [x for x in range (1, 51) if x % 3 == 0]
print(y)

st2 = "Print every word in this sentence that has an even number of letters"
SplitSt2 = st2.split()

for portion in SplitSt2:
    if (len(portion) % 2 == 0):
        print("even!")

for number in range(0, 101):
    if ((number % 3 == 0) and (number % 5 == 0)):
        print("FizzBuzz")
    elif (number % 3 == 0):
        print("Fizz")
    elif (number % 5 == 0):
        print("Buzz")
    else:
        print(number)


st3 = "Create a list of the first letters of every word in this string"
St3Split = st3.split()

for portion in St3Split:
    print(portion[0])







