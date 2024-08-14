#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("Input\\names\\invited_names.txt", mode="r") as the_names:
    names = the_names.readlines()

with open("Input\\Letters\\starting_letter.txt", mode="r") as the_letter:
    letter = the_letter.read()

for name in names:
    name = name.strip()
    with open(f"Output\\ReadyToSend\\letter_for_{name}.txt", mode="w") as output_letter:
        output_letter.write(letter.replace("[name]", name))





