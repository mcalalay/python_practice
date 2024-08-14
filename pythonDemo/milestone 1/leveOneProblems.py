def old_macdonald(name):
    first_half = name[:3]
    second_half = name[3:]

    return  first_half.capitalize() +second_half.capitalize()

def master_yoda(text):
    wordlist = text.split()
    reverse_word_list = wordlist[::-1]
    return " ".join(reverse_word_list)

print(master_yoda("I am home"))

print(old_macdonald("macdonalds"))

def almost_there(n):
    return (abs(100-n) <= 10) or (abs(200-n) <= 10)