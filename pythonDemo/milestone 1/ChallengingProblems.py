def spy_game(list):
    code = [0,0,7,"x"]
    for num in list:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1

print(spy_game([1,2,3,4,0,0,7]))

def count_primes(num):
    if num < 2:
        return 0
    primes = [2]
    x = 3
    while x <= num:
        for y in primes:
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2

    print(primes)
    return(len(primes))

print(count_primes(100))