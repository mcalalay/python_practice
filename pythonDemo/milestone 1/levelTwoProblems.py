def has_33(nums):
    for i in range (0, len(nums)-1):
        if nums[i:i+2] == [3,3]:
            return True

    return False

print(has_33([3, 3, 2, 3,2]))
print(has_33([3, 2, 2, 3,2]))

def paper_doll(text):
    result = ""
    for char in text:
        result +=char*3
    return result

def blackjack(a,b,c):

    if sum([a,b,c]) <= 21:
        return sum([a,b,c])
    elif 11 in [a,b,c] and sum([a,b,c]) <= 31:
        return sum([a,b,c])-10
    else:
        return "BUST"

def summer_69(arr):
    total = 0
    add = True

    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total
