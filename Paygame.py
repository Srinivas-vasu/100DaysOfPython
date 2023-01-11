import random
names_string = input("Give me everybody's names, separated by a comma and space. ")
names = names_string.split(", ")
i=0
len_of_names=len(names)
i=random.randint(0,len_of_names-1)
print(i)
pay_by=names[i]

print(f"{pay_by} is going to buy the meal today!")


