def lesser_of_two_evens(x,y):
    if (x % 2 ==0 and y % 2 == 0):
        return min(x,y)
    else:
        return max(x,y)

print(lesser_of_two_evens(100, 40))

def animal_crackers(text):
    wordlist = text.lower().split()
    return wordlist[0][0] == wordlist[1][0]

def makes_twenty(x , y):
    return x+y == 20 or x == 20 or y == 20
        