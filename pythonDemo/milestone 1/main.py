import re

my_baby= "Mary Charlene Campos"

print(my_baby[-1])
print(my_baby[5:13:2])
print (my_baby + "\n I love her")
print(len(my_baby))

print(my_baby[5:13])

last_name_of_my_baby = my_baby[14:]
first_name = my_baby[5:13]
print(type(last_name_of_my_baby))

print("SH" + last_name_of_my_baby)
print(first_name + " Calalay")
print((first_name + " Calalay\n")*10)
x = "Hello World"
print(x.upper())
print(x.split())

new_sentence = "Hi, the weather is kin?d of rainy today. " \
               "do you want some coffee?"
print(re.split(', ? o', new_sentence))
print(new_sentence.split(","))

print(" Mary {0} {1} {2}".format("Charlene", "Campos", "Regencia"))
print(" Mary {x} {z} {y}".format(x ="Charlene", y ="Campos", z="Regencia"))

result = 100000000000000/777
print ("The result was {}".format(result))
print (f"The result was {result:100.4f}".format(result))

name = "Charlene"
print(f"Hi, {name}")

x = "Python"
y = "!"
print("{} rules{}".format(x,y))