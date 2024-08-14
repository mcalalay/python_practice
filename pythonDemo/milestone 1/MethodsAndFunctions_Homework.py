def ran_check(num, low, high):
    if num in range(low, high+1):
        print(f"{num} is in range of low and high")
    else:
        print(f"{num} is not in range")

def up_lows(s):
    lowercase = 0
    uppercase = 0
    for char in s:
        if char.isupper():
            uppercase +=1
        elif char.islower():
            lowercase +=1
        else:
            pass
    print (f"original string: {s}")
    print (f"Lowercase count: {lowercase}")
    print(f"uppercase count: {uppercase}")

def unique_list(lst):
    seen_numbers = []
    for number in lst:
        if number not in seen_numbers:
            seen_numbers.append(number)
    return seen_numbers

sample_list = [1,2,3,-4]

x= map(lambda x :x*sample_list, sample_list)
print(x)

def palindrome(s):

    s = s.replace(" ", "")

    return s == s[::-1]

import string

def ispangram(str1, alphabet=string.ascii_letters_lowercase):

    alphaset = set(alphabet)
    str1 = str1.replace(" ", "")
    str1= str1.lower()
    str1 = set