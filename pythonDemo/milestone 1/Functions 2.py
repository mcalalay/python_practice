def myfunc(*args):
    for num in args:
        if num % 2 == 0:
            list_of_even = []
            list_of_even.append(num)
    return list_of_even

print(myfunc(1, 2, 3, 4, -2, -4))

def myfunc1(str):
    characters = []
    for i in str:

        if i % 2 == 0:
            characters.append(str[i].upper())
        else:
            characters.append(str[i].lower())

    return "".join(characters)


print(myfunc1("Anthropomorphism"))
