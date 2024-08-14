
myfile = open("myfile.txt")
print(myfile.read())
myfile.seek(0)
print(myfile.read())
myfile.seek(0)
print(myfile.readlines())
myfile.close()
with open("myfile.txt") as my_new_file:
    contents = my_new_file.read()
    print(contents)
    print(contents)

with open("myfile.txt", mode = "w+") as f:
    contents = f.write('Good morning! Overwriting the old file,'
                                 'thanks!')
with open("myfile.txt", mode="r") as f:
        contents = f.read()
        print(contents)

with open("myfile.txt", mode = "a") as f:
        f.write("\nadditional notes, Matthew created this file.")
        print(contents)