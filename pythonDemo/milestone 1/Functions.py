employees = [ ("Abby", 1000), ("Marco", 600), ("Billy", 900)]

def employee_check(employees):
    highest_work_hours = 0
    employee_of_the_month = ""
    for person,hours in employees:
        if highest_work_hours < hours:
            highest_work_hours = hours
            employee_of_the_month=person
        else:
            pass
    return highest_work_hours, employee_of_the_month

print(employee_check(employees))





from random import shuffle

def shuffle_list(myList):
    shuffle(myList)
    return(myList)

def player_guess():
    guess = " "
    while guess not in ["0", "1", "2"]:
        guess = input("Pick a number: 0, 1, 2\n")
    return int(guess)

def checker(shuffled_list, guess):
    if shuffled_list[guess] == "0":
        print("you lucky bastard")
    else:
        print("better luck next time idiot")
        print(shuffled_list)

myList = [" ", "0", " "]
shuffled_list = shuffle_list(myList)
guess = player_guess()
checker(shuffled_list, guess)


def myfunct(*args, **kwargs):
    print(f"I would like {args[0]} {kwargs['food']}")

myfunct(10 , 20 , 30, fruit= "mango", food ="hotdog")

def adder(*args):
    return(sum(*args))
print(adder(1 , 2, 3, 4, 5, 6))


