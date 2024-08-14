my_list = [2.001, "Charlene", 351]
print(len(my_list))

print(my_list[1:])

my_list_2 = ["good", "morning"]
my_list_3 = ["baby", "love"]

combined_list = my_list_2 + my_list_3

print(combined_list)

combined_list.append("i love you")
print(combined_list)

print(combined_list.pop())
print(combined_list.pop(-2))
print(combined_list)

alphabetical_list = ["a", "y", "p", "q"]
num_list = [1, 3, 78,14,12, 25,31,54,36,7456]
num_list.sort()
alphabetical_list.sort()
print(num_list)
print(alphabetical_list)


my_dict={"baby love":"Charlene Campos", "dog":"Cutie and Coco", "home":"baby love",
            "house":"pasig", "anotherone":{"hotdog":"cheesedog"}}

print(my_dict["anotherone"]["hotdog"])

my_dict['asawa_ko'] = "Charlene Calalay"
print(my_dict)


tpl = (1 , 2 ,3)
print(len(tpl))

tpl = (1, 1, 1, 2, 2, 2,2 , 3, my_dict)
print(tpl.index(2))
print(tpl[-1])

